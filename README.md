



samples({
  loop0: 'https://raw.githubusercontent.com/jakubstenc/sudo_apt_get_music/main/commit_merge/commit_2.wav',
  loop1: 'https://raw.githubusercontent.com/jakubstenc/sudo_apt_get_music/main/commit_merge/merge.wav',
});

setcpm(20)

note("<[c2 c3]*4 [bb1 bb2]*4 [f2 f3]*4 [eb2 eb3]*4>")
  // We use <loop0!4 loop1!4> to repeat loop0 4 times, then loop1 4 times
  .sound("bd bd bd - <loop0!4 loop1!4> - ") 
  .room(.2)
  .gain(0.9)

