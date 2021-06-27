
# Sublime plugin to hide comments

Small plugin for Sublime Text 3 to fold & unfold comments with a shortcut:

![](https://github.com/MarieMalarme/sublime_plugin_hide_comments/blob/master/images/unfolded_comments.png)
![](https://github.com/MarieMalarme/sublime_plugin_hide_comments/blob/master/images/folded_comments.png)


## Shortcut
The shortcut by default is `Cmd + ;` ; change it in the file `Default.sublime-keymap` if you want to make it custom!


## Fold icon
To my great despair, it doesn't seem possible to completely change the magnificent yellow fold icon as it was suggested [here for ST2](https://stackoverflow.com/questions/27474034/hide-code-folding-icon-in-sublimetext), though it is possible to change its background color by editing the color scheme file of your theme, as explained [here](https://forum.sublimetext.com/t/big-ugly-distracting-yellow-icon-that-replaces-folded-text/13350/16):
- open the corresponding file - or create one if there's none: <br />
  `Sublime Text 3 → Packages → User → ThemeName.sublime-color-scheme`
- add the following lines, setting up the color you want for the icon background (note that the dots' color doesn't seem to be customizable):

  ```
  {
    "globals":
      {
        "fold_marker": "grey"
      }
  }
  ```
