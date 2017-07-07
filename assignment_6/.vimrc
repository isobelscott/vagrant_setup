" " need vim

sudo apt-get install vim

" " make it look good
set bg=dark
set backspace=2

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
