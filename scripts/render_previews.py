"""Encode QA demonstrations from the exact pet atlas; never alter pet pixels."""
import argparse
import json
import subprocess
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import imageio_ffmpeg

STATES = {
    'idle': [280,110,110,140,140,320],
    'running-right': [120]*7+[220],
    'running-left': [120]*7+[220],
    'waving': [140]*3+[280],
    'jumping': [140]*4+[280],
    'failed': [140]*7+[240],
    'waiting': [150]*5+[260],
    'running': [120]*5+[220],
    'review': [150]*5+[280],
}

def gif(frames, durations, path):
    frames[0].save(path, save_all=True, append_images=frames[1:],
                   duration=durations, loop=0, disposal=2, optimize=False)

def main():
    p=argparse.ArgumentParser()
    p.add_argument('atlas')
    p.add_argument('--output-dir', required=True)
    a=p.parse_args()
    out=Path(a.output_dir); out.mkdir(parents=True,exist_ok=True)
    atlas=Image.open(a.atlas).convert('RGBA')
    def cell(row,col):
        return atlas.crop((col*192,row*208,(col+1)*192,(row+1)*208))
    frames_root=out/'atlas-frames'
    all_frames=[]; all_durations=[]
    font=ImageFont.load_default(size=15)
    for row,(state,durations) in enumerate(STATES.items()):
        directory=frames_root/state; directory.mkdir(parents=True,exist_ok=True)
        for col,duration in enumerate(durations):
            sprite=cell(row,col)
            sprite.save(directory/f'{col:02d}.png')
            labeled=Image.new('RGB',(240,256),'#f1f3f5')
            labeled.paste(sprite,(24,12),sprite)
            ImageDraw.Draw(labeled).text((12,231),state,fill='#222222',font=font)
            all_frames.append(labeled); all_durations.append(duration)
    gif(all_frames,all_durations,out/'all-states.gif')
    jump=[cell(0,i) for i in range(6)]+[cell(4,i) for i in range(5)]+[cell(0,i) for i in range(6)]
    gif(jump,STATES['idle']+STATES['jumping']+STATES['idle'],out/'idle-jump-idle.gif')
    look=[cell(9+c//8,c%8) for c in range(16)]
    gif(look,[170]*16,out/'look-loop.gif')
    stills=Image.new('RGB',(4*216,248),'#f1f3f5')
    draw=ImageDraw.Draw(stills)
    for k,c in enumerate([0,1,2,4]):
        sprite=cell(7,c); stills.paste(sprite,(k*216+12,8),sprite)
        draw.text((k*216+12,224),f'curl frame {c+1}',fill='#222222',font=font)
    stills.save(out/'curl-motion-stills.png')
    ffmpeg=imageio_ffmpeg.get_ffmpeg_exe()
    subprocess.run([ffmpeg,'-y','-i',str(out/'all-states.gif'),'-vf','scale=480:512:flags=neighbor',
                    '-c:v','libx264','-pix_fmt','yuv420p','-movflags','+faststart',str(out/'all-states.mp4')],
                   check=True,stdout=subprocess.DEVNULL,stderr=subprocess.PIPE)
    (out/'preview-manifest.json').write_text(json.dumps({'source_atlas':str(Path(a.atlas).resolve()),
        'standard_states':list(STATES),'four_stills':'curl-motion-stills.png',
        'all_state_gif':'all-states.gif','all_state_mp4':'all-states.mp4',
        'transition':'idle-jump-idle.gif','look_loop':'look-loop.gif'},indent=2))
    print(json.dumps({'ok':True,'frames_root':str(frames_root),'output_dir':str(out)}))

if __name__=='__main__': main()
