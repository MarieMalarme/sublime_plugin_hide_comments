from sublime import Region
import sublime_plugin

# name the class to match the command "hide_comments"
# set in the files "Default.sublime-commands" & "Default.sublime-keymap"
# "hide_comments" converted in pascal case + "Command" → "HideCommentsCommand"
class HideCommentsCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    view = self.view
    comments = view.find_by_selector('comment')
    comments_already_folded = view.unfold(comments[0])

    if not comments_already_folded:
      for comment_index in range(0, len(comments)):
        # set the beggining & end of the region to fold:
        # both values are integers corresponding to the characters' positions in the file
        comment_region_beginning = comments[comment_index].a
        comment_region_end = comments[comment_index].b

        # walk through the following comments to determine 
        # if it is a multiline comment block
        for next_comment_index in range(comment_index + 1, len(comments)):
          # get the region between the end of the current comment
          # and the beggining of the next one
          interval_region = Region(comment_region_end, comments[next_comment_index].a)
          # check if the interval region is only composed of whitespaces,
          # meaning that comments are in the same multiline comment block
          is_same_comment_block = view.substr(interval_region).isspace()
          if is_same_comment_block:
            # update the end of the comment block to fold to the end of the next comment 
            comment_region_end = comments[next_comment_index].b

        # fold the targetted comment block & remove the last character
        # to keep the line-break and have the fold icon on a full line
        view.fold(Region(comment_region_beginning, comment_region_end - 1))
    else:
      view.unfold(comments)
