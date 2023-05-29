#############################################################################
# Generated by PAGE version 7.1
#  in conjunction with Tcl version 8.6
#  Jan 20, 2022 09:46:44 AM CST  platform: Linux
set vTcl(timestamp) ""
if {![info exists vTcl(borrow)]} {
    tk_messageBox -title Error -message  "You must open project files from within PAGE."
    exit}


set image_list { 
}
vTcl:create_project_images $image_list   ;# In image.tcl

if {!$vTcl(borrow) && !$vTcl(template)} {

set vTcl(actual_gui_font_dft_desc)  TkDefaultFont
set vTcl(actual_gui_font_dft_name)  TkDefaultFont
set vTcl(actual_gui_font_text_desc)  TkTextFont
set vTcl(actual_gui_font_text_name)  TkTextFont
set vTcl(actual_gui_font_fixed_desc)  TkFixedFont
set vTcl(actual_gui_font_fixed_name)  TkFixedFont
set vTcl(actual_gui_font_menu_desc)  TkMenuFont
set vTcl(actual_gui_font_menu_name)  TkMenuFont
set vTcl(actual_gui_font_tooltip_desc)  TkDefaultFont
set vTcl(actual_gui_font_tooltip_name)  TkDefaultFont
set vTcl(actual_gui_font_treeview_desc)  TkDefaultFont
set vTcl(actual_gui_font_treeview_name)  TkDefaultFont
set vTcl(actual_gui_bg) #d9d9d9
set vTcl(actual_gui_fg) #000000
set vTcl(actual_gui_analog) #5e5e5e
set vTcl(actual_gui_menu_analog) #ececec
set vTcl(actual_gui_menu_bg) #d9d9d9
set vTcl(actual_gui_menu_fg) #000000
set vTcl(complement_color) #d9d9d9
set vTcl(analog_color_p) #d9d9d9
set vTcl(analog_color_m) #ececec
set vTcl(active_fg) #000000
set vTcl(actual_gui_menu_active_bg)  #ececec
set vTcl(actual_gui_menu_active_fg)  #000000
set vTcl(pr,autoalias) 1
set vTcl(pr,relative_placement) 0
set vTcl(mode) Absolute
}




proc vTclWindow.top61 {base} {
    global vTcl
    if {$base == ""} {
        set base .top61
    }
    if {[winfo exists $base]} {
        wm deiconify $base; return
    }
    set top $base
    set target $base
    ###################
    # CREATING WIDGETS
    ###################
    vTcl::widgets::core::toplevel::createCmd $top -class Toplevel \
        -background $vTcl(actual_gui_bg) -highlightcolor black 
    wm focusmodel $top passive
    wm geometry $top 764x506+284+238
    update
    # set in toplevel.wgt.
    global vTcl
    global img_list
    set vTcl(save,dflt,origin) 0
    wm maxsize $top 3585 1050
    wm minsize $top 1 1
    wm overrideredirect $top 0
    wm resizable $top 1 1
    wm deiconify $top
    set toptitle "MainForm"
    wm title $top $toptitle
    namespace eval ::widgets::${top}::ClassOption {}
    set ::widgets::${top}::ClassOption(-toptitle) $toptitle
    vTcl:DefineAlias "$top" "MainForm" vTcl:Toplevel:WidgetProc "" 1
    set vTcl(real_top) {}
    vTcl:withBusyCursor {
    button $top.but45 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -command on_btnExit \
        -font {-family {DejaVu Sans} -size 10 -weight bold -slant italic -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black -text Exit 
    vTcl:DefineAlias "$top.but45" "btnExit" vTcl:WidgetProc "MainForm" 1
    checkbutton $top.che46 \
        -activebackground #f9f9f9 -activeforeground black -anchor w \
        -background $vTcl(actual_gui_bg) -borderwidth 2 \
        -font {-family {DejaVu Sans} -size 10 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black -justify left \
        -relief ridge -text {Has second form been run?} -variable che46 
    vTcl:DefineAlias "$top.che46" "Checkbutton1" vTcl:WidgetProc "MainForm" 1
    label $top.lab47 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -borderwidth 2 \
        -font {-family {DejaVu Sans} -size 10 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black -relief ridge \
        -text Label -textvariable SecondFormData 
    vTcl:DefineAlias "$top.lab47" "Label1" vTcl:WidgetProc "MainForm" 1
    set SecondFormData {Label}
    label $top.lab48 \
        -activebackground #f9f9f9 -activeforeground black -anchor w \
        -background $vTcl(actual_gui_bg) \
        -font {-family {DejaVu Sans} -size 10 -weight bold -slant italic -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black \
        -text {Data passed from second form:} 
    vTcl:DefineAlias "$top.lab48" "Label2" vTcl:WidgetProc "MainForm" 1
    button $top.but49 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -command on_btnLaunch \
        -font {-family {DejaVu Sans} -size 10 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black \
        -text {Launch Second Form} 
    vTcl:DefineAlias "$top.but49" "btnLaunch" vTcl:WidgetProc "MainForm" 1
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.but45 \
        -in $top -x 590 -y 30 -width 89 -relwidth 0 -height 29 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.che46 \
        -in $top -x 90 -y 100 -width 263 -relwidth 0 -height 31 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.lab47 \
        -in $top -x 90 -y 220 -width 418 -relwidth 0 -height 31 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.lab48 \
        -in $top -x 90 -y 190 -width 323 -relwidth 0 -height 21 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.but49 \
        -in $top -x 90 -y 300 -width 225 -relwidth 0 -height 31 -relheight 0 \
        -anchor nw -bordermode ignore 
    } ;# end vTcl:withBusyCursor 

    vTcl:FireEvent $base <<Ready>>
}

proc vTclWindow.top90 {base} {
    global vTcl
    if {$base == ""} {
        set base .top90
    }
    if {[winfo exists $base]} {
        wm deiconify $base; return
    }
    set top $base
    set target $base
    ###################
    # CREATING WIDGETS
    ###################
    vTcl::widgets::core::toplevel::createCmd $top -class Toplevel \
        -background cornflowerblue -highlightcolor black 
    wm focusmodel $top passive
    wm geometry $top 760x506+835+439
    update
    # set in toplevel.wgt.
    global vTcl
    global img_list
    set vTcl(save,dflt,origin) 0
    wm maxsize $top 3585 1050
    wm minsize $top 1 1
    wm overrideredirect $top 0
    wm resizable $top 1 1
    wm deiconify $top
    set toptitle "Second Form"
    wm title $top $toptitle
    namespace eval ::widgets::${top}::ClassOption {}
    set ::widgets::${top}::ClassOption(-toptitle) $toptitle
    vTcl:DefineAlias "$top" "ChildForm" vTcl:Toplevel:WidgetProc "" 1
    set vTcl(real_top) {}
    vTcl:withBusyCursor {
    entry $top.ent51 \
        -background white -font TkFixedFont -foreground $vTcl(actual_gui_fg) \
        -highlightcolor black -insertbackground black -selectbackground blue \
        -selectforeground white -textvariable PassBack -width 516 
    vTcl:DefineAlias "$top.ent51" "Entry1" vTcl:WidgetProc "ChildForm" 1
    button $top.but52 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -command on_btnDismiss \
        -font {-family {DejaVu Sans} -size 10 -weight bold -slant italic -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black -text Dismiss 
    vTcl:DefineAlias "$top.but52" "btnDismiss" vTcl:WidgetProc "ChildForm" 1
    label $top.lab53 \
        -activebackground #6495ed -activeforeground black -background #6495ed \
        -font {-family {DejaVu Sans} -size 12 -weight bold -slant italic -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black \
        -text {This is the Second Form!} 
    vTcl:DefineAlias "$top.lab53" "Label1_1" vTcl:WidgetProc "ChildForm" 1
    label $top.lab54 \
        -activebackground #f9f9f9 -activeforeground black -anchor w \
        -background #6495ed \
        -font {-family {DejaVu Sans} -size 10 -weight bold -slant italic -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black \
        -text {Data to pass back to the Main form:} 
    vTcl:DefineAlias "$top.lab54" "Label2_1" vTcl:WidgetProc "ChildForm" 1
    label $top.lab55 \
        -activebackground #6495ed -activeforeground black -anchor e \
        -background #6495ed \
        -font {-family {DejaVu Sans} -size 10 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black \
        -text {Times this form has been shown:} 
    vTcl:DefineAlias "$top.lab55" "Label3" vTcl:WidgetProc "ChildForm" 1
    label $top.lab56 \
        -activebackground #f9f9f9 -activeforeground black -background #6495ed \
        -font {-family {DejaVu Sans} -size 12 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black -text Label \
        -textvariable RunCount 
    vTcl:DefineAlias "$top.lab56" "Label4" vTcl:WidgetProc "ChildForm" 1
    set RunCount {Label}
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.ent51 \
        -in $top -x 120 -y 240 -width 516 -relwidth 0 -height 31 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.but52 \
        -in $top -x 620 -y 20 -width 99 -relwidth 0 -height 29 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.lab53 \
        -in $top -x 110 -y 50 -width 466 -relwidth 0 -height 49 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.lab54 \
        -in $top -x 120 -y 210 -width 416 -relwidth 0 -height 19 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.lab55 \
        -in $top -x 120 -y 120 -width 266 -relwidth 0 -height 19 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.lab56 \
        -in $top -x 390 -y 115 -width 66 -relwidth 0 -height 29 -relheight 0 \
        -anchor nw -bordermode ignore 
    } ;# end vTcl:withBusyCursor 

    vTcl:FireEvent $base <<Ready>>
}

proc 36 {args} {return 1}


Window show .
set btop1 ""
if {$vTcl(borrow)} {
    set btop1 .bor[expr int([expr rand() * 100])]
    while {[lsearch $btop1 $vTcl(tops)] != -1} {
        set btop1 .bor[expr int([expr rand() * 100])]
    }
}
set vTcl(btop) $btop1
Window show .top61 $btop1
if {$vTcl(borrow)} {
    $btop1 configure -background plum
}
set btop2 ""
if {$vTcl(borrow)} {
    set btop2 .bor[expr int([expr rand() * 100])]
    while {[lsearch $btop2 $vTcl(tops)] != -1} {
        set btop2 .bor[expr int([expr rand() * 100])]
    }
}
set vTcl(btop) $btop2
Window show .top90 $btop2
if {$vTcl(borrow)} {
    $btop2 configure -background plum
}

