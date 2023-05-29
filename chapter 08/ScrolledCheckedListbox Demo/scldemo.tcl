#############################################################################
# Generated by PAGE version 7.6
#  in conjunction with Tcl version 8.6
#  Dec 21, 2022 06:01:01 AM CST  platform: Linux
set vTcl(timestamp) ""
if {![info exists vTcl(borrow)]} {
    ::vTcl::MessageBox -title Error -message  "You must open project files from within PAGE."
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
########################################### 
set vTcl(actual_gui_bg) #d9d9d9
set vTcl(actual_gui_fg) #000000
set vTcl(actual_gui_analog) #ececec
set vTcl(actual_gui_menu_analog) #ececec
set vTcl(actual_gui_menu_bg) #d9d9d9
set vTcl(actual_gui_menu_fg) #000000
set vTcl(complement_color) gray40
set vTcl(analog_color_p) #c3c3c3
set vTcl(analog_color_m) beige
set vTcl(tabfg1) black
set vTcl(tabfg2) black
set vTcl(actual_gui_menu_active_bg)  #ececec
set vTcl(actual_gui_menu_active_fg)  #000000
########################################### 
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
    set target $base
    ###################
    # CREATING WIDGETS
    ###################
    vTcl::widgets::core::toplevel::createCmd $top -class Toplevel \
        -background bisque4 
    wm focusmodel $top passive
    wm geometry $top 706x653+689+265
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
    set toptitle "ScrolledCheckedListbox Demo"
    wm title $top $toptitle
    namespace eval ::widgets::${top}::ClassOption {}
    set ::widgets::${top}::ClassOption(-toptitle) $toptitle
    vTcl:DefineAlias "$top" "Main" vTcl:Toplevel:WidgetProc "" 1
    set vTcl(real_top) {}
    button "$top.but47" \
        -activebackground $vTcl(analog_color_m) -activeforeground black \
        -background $vTcl(actual_gui_bg) -borderwidth 2 -command "on_btnExit" \
        -compound left \
        -font "-family {DejaVu Sans} -size 10 -weight bold -slant roman -underline 0 -overstrike 0" \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black -text "Exit" 
    vTcl:DefineAlias "$top.but47" "btnExit" vTcl:WidgetProc "Main" 1
### SPOT dump_widget_opt A
    message "$top.mes48" \
        -background $vTcl(actual_gui_bg) -font "TkDefaultFont" \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black -padx 1 \
        -pady 1 -text "Message" -width 322 
    vTcl:DefineAlias "$top.mes48" "Message1" vTcl:WidgetProc "Main" 1
### SPOT dump_widget_opt A
    frame "$top.fra49" \
        -borderwidth 2 -relief groove -background $vTcl(actual_gui_bg) \
        -height 345 -width 305 
    vTcl:DefineAlias "$top.fra49" "Frame1" vTcl:WidgetProc "Main" 1
### SPOT dump_widget_opt A
    set site_3_0 $top.fra49
    vTcl::widgets::ttk::custom::CreateCmd "$site_3_0.cus50" \
        -background $vTcl(actual_gui_bg) -height 75 -highlightcolor black \
        -width 125 
    vTcl:DefineAlias "$site_3_0.cus50" "Custom1" vTcl:WidgetProc "Main" 1
### SPOT dump_widget_opt A
    place $site_3_0.cus50 \
        -in $site_3_0 -x 0 -y 0 -width 0 -relwidth 1 -height 0 -relheight 1 \
        -anchor nw -bordermode ignore 
    button "$top.but51" \
        -activebackground $vTcl(analog_color_m) -activeforeground black \
        -background $vTcl(actual_gui_bg) -borderwidth 2 \
        -command "on_btnGetChecks" -compound left \
        -font "-family {DejaVu Sans} -size 10 -weight bold -slant roman -underline 0 -overstrike 0" \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black \
        -text "Get Checks" 
    vTcl:DefineAlias "$top.but51" "btnGetChecks" vTcl:WidgetProc "Main" 1
### SPOT dump_widget_opt A
    button "$top.but52" \
        -activebackground $vTcl(analog_color_m) -activeforeground black \
        -background $vTcl(actual_gui_bg) -borderwidth 2 \
        -command "on_btnClearChecks" -compound left \
        -font "-family {DejaVu Sans} -size 10 -weight bold -slant roman -underline 0 -overstrike 0" \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black \
        -text "Clear Checks" 
    vTcl:DefineAlias "$top.but52" "btnClearChecks" vTcl:WidgetProc "Main" 1
### SPOT dump_widget_opt A
    button "$top.but53" \
        -activebackground $vTcl(analog_color_m) -activeforeground black \
        -background $vTcl(actual_gui_bg) -borderwidth 2 \
        -command "on_btnSwitchMode" -compound left \
        -font "-family {DejaVu Sans} -size 10 -weight bold -slant roman -underline 0 -overstrike 0" \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black \
        -text "Switch Mode" 
    vTcl:DefineAlias "$top.but53" "btnSwitchMode" vTcl:WidgetProc "Main" 1
### SPOT dump_widget_opt A
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.but47 \
        -in $top -x 540 -y 40 -width 103 -relwidth 0 -height 33 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.mes48 \
        -in $top -x 40 -y 200 -width 322 -relwidth 0 -height 71 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.fra49 \
        -in $top -x 40 -y 290 -width 305 -relwidth 0 -height 345 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.but51 \
        -in $top -x 410 -y 320 -width 163 -relwidth 0 -height 33 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.but52 \
        -in $top -x 410 -y 380 -width 163 -relwidth 0 -height 33 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.but53 \
        -in $top -x 420 -y 480 -width 153 -relwidth 0 -height 33 -relheight 0 \
        -anchor nw -bordermode ignore 

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
