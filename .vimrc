 minimal vimrc for new vim users to start with.
 "
 "" Referenced here:
 http://www.benorenstein.com/blog/your-first-vimrc-should-be-nearly-empty/

 " Original Author:  Bram Moolenaar <Bram@vim.org>
 " " Made more minimal by:  Ben Orenstein
 " " Last change:            2012 Jan 20
 " "
 " " To use it, copy it to
 " "     for Unix and OS/2:  ~/.vimrc
 " "  for MS-DOS and Win32:  $VIM\_vimrc
 " "
 " "  If you don't understand a setting in here, just type ':h setting'.
 "
 " " Use Vim settings, rather than Vi settings (much better!).
 " " This must be first, because it changes other options as a side effect.
 " set nocompatible
 "
 " " Make backspace behave in a sane manner.
 set backspace=indent,eol,start
 "
 " " Switch syntax highlighting on
 syntax on
 "
 " " Enable file type detection and do language-dependent indenting.
 filetype plugin indent on

 " .vimrc
set tabstop=4         " number of visual spaces per TAB
set softtabstop=4    " number of spaces in tab when editing
set expandtab          " tabs are spaces