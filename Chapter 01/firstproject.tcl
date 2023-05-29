#############################################################################
# Generated by PAGE version 7x
#  in conjunction with Tcl version 8.6
#  Oct 15, 2021 03:34:38 AM CDT  platform: Linux
set vTcl(timestamp) ""
if {![info exists vTcl(borrow)]} {
    tk_messageBox -title Error -message  "You must open project files from within PAGE."
    exit}


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
set vTcl(actual_gui_analog) #ececec
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




proc vTclWindow.top1 {base} {
    global vTcl
    if {$base == ""} {
        set base .top1
    }
    if {[winfo exists $base]} {
        wm deiconify $base; return
    }
    set top $base
    ###################
    # CREATING WIDGETS
    ###################
    vTcl::widgets::core::toplevel::createCmd $top -class Toplevel \
        -background $vTcl(actual_gui_bg) -highlightcolor #000000 
    wm focusmodel $top passive
    wm geometry $top 600x450+881+376
    update
    # set in toplevel.wgt.
    global vTcl
    global img_list
    set vTcl(save,dflt,origin) 0
    wm maxsize $top 4225 1410
    wm minsize $top 1 1
    wm overrideredirect $top 0
    wm resizable $top 1 1
    wm deiconify $top
    set toptitle "Toplevel 1"
    wm title $top $toptitle
    namespace eval ::widgets::${top}::ClassOption {}
    set ::widgets::${top}::ClassOption(-toptitle) $toptitle
    vTcl:DefineAlias "$top" "Firstproject" vTcl:Toplevel:WidgetProc "" 1
    set vTcl(real_top) {}
    vTcl:withBusyCursor {
    button $top.but46 \
        -background $vTcl(actual_gui_bg) -borderwidth 2 -command on_btnExit \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black -text Exit 
    vTcl:DefineAlias "$top.but46" "btnExit" vTcl:WidgetProc "Firstproject" 1
    label $top.lab47 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(actual_gui_bg) -foreground $vTcl(actual_gui_fg) \
        -highlightcolor #000000 -text {This is a STATIC Label} 
    vTcl:DefineAlias "$top.lab47" "lblStatic" vTcl:WidgetProc "Firstproject" 1
    label $top.lab48 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(actual_gui_bg) -foreground $vTcl(actual_gui_fg) \
        -highlightcolor #000000 -relief sunken -text Label \
        -textvariable ::vTcl::DynamicLabelText 
    vTcl:DefineAlias "$top.lab48" "lblDynamic" vTcl:WidgetProc "Firstproject" 1
    set ::vTcl::DynamicLabelText {Label}
    entry $top.ent49 \
        -background white -font TkFixedFont -foreground $vTcl(actual_gui_fg) \
        -highlightcolor #000000 -insertbackground black \
        -selectbackground #c3c3c3 -selectforeground #000000 \
        -textvariable ::vTcl::EntryData -width 256 
    vTcl:DefineAlias "$top.ent49" "Entry1" vTcl:WidgetProc "Firstproject" 1
    button $top.but50 \
        -background $vTcl(actual_gui_bg) -borderwidth 2 \
        -command on_btnGrabEntry -foreground $vTcl(actual_gui_fg) \
        -highlightcolor black -text {Grab Entry} 
    vTcl:DefineAlias "$top.but50" "btnGrabEntry" vTcl:WidgetProc "Firstproject" 1
    frame $top.fra51 \
        -borderwidth 2 -relief groove -background $vTcl(actual_gui_bg) \
        -height 75 -highlightcolor #000000 -width 125 
    vTcl:DefineAlias "$top.fra51" "Frame1" vTcl:WidgetProc "Firstproject" 1
    set site_3_0 $top.fra51
    label $site_3_0.lab52 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -anchor w -background $vTcl(actual_gui_bg) \
        -foreground $vTcl(actual_gui_fg) -highlightcolor #000000 \
        -text {Do You Like Mushrooms?} 
    vTcl:DefineAlias "$site_3_0.lab52" "lblRbQuestion" vTcl:WidgetProc "Firstproject" 1
    radiobutton $site_3_0.rad53 \
        -anchor w -background $vTcl(actual_gui_bg) -command on_rbClick \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black -justify left \
        -text NO -value 0 -variable selectedButton 
    vTcl:DefineAlias "$site_3_0.rad53" "RadiobuttonNo" vTcl:WidgetProc "Firstproject" 1
    radiobutton $site_3_0.rad54 \
        -anchor w -background $vTcl(actual_gui_bg) -command on_rbClick \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black -justify left \
        -text YES -value 1 -variable selectedButton 
    vTcl:DefineAlias "$site_3_0.rad54" "RadiobuttonYes" vTcl:WidgetProc "Firstproject" 1
    label $site_3_0.lab55 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(actual_gui_bg) -foreground $vTcl(actual_gui_fg) \
        -highlightcolor #000000 -relief ridge -text Label \
        -textvariable ::vTcl::RbSelectDisplay 
    vTcl:DefineAlias "$site_3_0.lab55" "lblRbResponse" vTcl:WidgetProc "Firstproject" 1
    place $site_3_0.lab52 \
        -in $site_3_0 -x 10 -y 10 -width 206 -relwidth 0 -height 21 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.rad53 \
        -in $site_3_0 -x 30 -y 43 -width 152 -relwidth 0 -anchor nw \
        -bordermode ignore 
    place $site_3_0.rad54 \
        -in $site_3_0 -x 30 -y 70 -width 152 -relwidth 0 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab55 \
        -in $site_3_0 -x 20 -y 110 -width 196 -relwidth 0 -height 29 \
        -relheight 0 -anchor nw -bordermode ignore 
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.but46 \
        -in $top -x 480 -y 10 -width 83 -relwidth 0 -height 33 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.lab47 \
        -in $top -x 150 -y 50 -width 229 -relwidth 0 -height 21 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.lab48 \
        -in $top -x 120 -y 100 -width 346 -relwidth 0 -height 29 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.ent49 \
        -in $top -x 90 -y 190 -width 256 -relwidth 0 -height 23 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.but50 \
        -in $top -x 360 -y 185 -width 94 -relwidth 0 -height 29 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.fra51 \
        -in $top -x 70 -y 260 -width 235 -relwidth 0 -height 155 -relheight 0 \
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
Window show .top1 $btop1
if {$vTcl(borrow)} {
    $btop1 configure -background plum
}
