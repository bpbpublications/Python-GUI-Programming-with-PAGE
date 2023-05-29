#
# "NotSoDark" theme.
# -------------------------------
# A semi-dark theme originally created for users of PAGE
# -------------------------------
# Inspired by the Clam, Alt and other themes.
# Written by G.D. Walters
# Copyright 2022,2023 by G.D. Walters  <thedesignatedgeek@gmail.com>
#
#====================================================
# Version 0.1.05.1
#====================================================
# Still to do: 12/30/2022
# ---------------------------------------------------

#   X 12/30/2022 - Find out why buttons don't shift image on click
#   X 12/30/2022 - TCombobox select highlight not working correctly
#   X 12/30/2022 - TButton mouse over color too bright
#   X 12/30/2022 - TEntry - on disabled, darken the field color
#   X 12/30/2022 - TSpin  - change background to -bgcolor
#   * TSpin  - on disabled, darken the field color
#   * Try to work with PNotebook
#   * Try to incorporate graphics for TCheck & TRadio
#   * Support all states for all widgets
#   * Go through color list and delete those that aren't used
#   * Tweek the colors
#   * Find out why file does not run on PAGE 8.0c
#====================================================
# Change log
#----------------------------------------------------
# 31/12/2022 - attempt to add tab placement style support for TNotebook (see README.txt)
# 01/01/2023 - attempt to add flat and sunken styles for TFrame
# 01/08/2023 - Changed selectbackground and selectforeground for TEntry.
# 01/09/2023 - Attempt to add configuration for TCombobox popdown.
#----------------------------------------------------

package require Tk 8.6



namespace eval ttk::theme::notsodark {
	variable version 0.1.05.1
	package provide ttk::theme::notsodark $version
	variable colors
	array set colors {
		-disabledfg		gray54
		-frame  		black
		-window  		"#ffffff"
		-dark			black
		-darker 		"#c3c3c3"
		-darkcolor      "#000000"
		-lighter		"#eeebe7"
		-lightcolor     snow
		-selectbg		"#4a6984"
		-selectfg		"#ffffff"
		-selectbackground   "#4a6984"
		-selectforeground   "#ffffff"
		-alternate			"#aaaaaa"
		-disabledcolor  gray54
		-bgcolor        "#919191"
		-fgcolor        black
		-activebgcolor  gray66
		-troughcolor    gray45
		-barcolor       royalblue3
		-fieldbgcolor   gray56
		-fieldfgcolor   deepskyblue
		-bordercolor    dimgray
		-tvwindow       lightgoldenrod3
		-tvwindowdisabled  PeachPuff3
	}

	# defined but unused
	#		-darkest		"#9e9a91"
	#		-lightest 		"#ffffff"
	#		-altindicator		"#aaaaaa"
	#		-disabledaltindicator	"#a0a0a0"
	#		-activefgcolor  gray5
	#		-bordercolor2   "#414141"


	# Settings
	ttk::style theme create notsodark -parent clam -settings {

		ttk::style configure "." \
			-background $colors(-bgcolor) \
			-foreground $colors(-fgcolor) \
			-bordercolor $colors(-frame) \
			-darkcolor $colors(-darkcolor) \
			-lightcolor $colors(-lightcolor) \
			-troughcolor $colors(-troughcolor) \
			-selectbackground $colors(-selectbackground) \
			-selectforeground $colors(-selectforeground) \
			-barcolor $colors(-barcolor) \
			-selectborderwidth 0 \
			-borderwidth 2 \
			-font TkDefaultFont \
			;

		ttk::style map "." \
			-background [list disabled $colors(-disabledcolor) \
			active $colors(-activebgcolor)] \
			-foreground [list disabled $colors(-disabledfg)] \
			-selectbackground [list  !focus $colors(-darkcolor)] \
			-selectforeground [list  !focus white] \
			-embossed [list disabled 1]
		;

		# -selectbackground [list  !focus "#847d73"]
		# --------------------------------------------------
		# TButton
		ttk::style configure TButton \
			-anchor center -width -11 -padding "1 1" -relief raised \
			-shiftrelief 2 -highlightthickness 1 -highlightcolor $colors(-frame)

		ttk::style map TButton -relief {
			{pressed !disabled} sunken
			{active !disabled} 	raised
			} -highlightcolor {alternate black}

			ttk::style map TButton \
				-background [list \
					disabled $colors(-disabledcolor) \
					pressed $colors(-darker) \
					active $colors(-activebgcolor)] \
					-lightcolor [list pressed $colors(-darker)] \
					-darkcolor [list pressed $colors(-darker)] \
					-bordercolor [list alternate "#000000"] \
					;

				# --------------------------------------------------
				# Toolbutton (special style for TButton)
				# --------------------------------------------------
				ttk::style configure Toolbutton \
					-anchor center -padding 2 -relief flat \
					-shiftrelief 2 -highlightthickness 1 \
					-highlightcolor $colors(-frame)

				ttk::style map Toolbutton \
					-relief [list \
						disabled flat \
						selected sunken \
						pressed sunken \
						active raised] \
						-background [list \
							disabled $colors(-disabledcolor) \
							pressed $colors(-darker) \
							active $colors(-activebgcolor)] \
							-lightcolor [list pressed $colors(-darker)] \
							-darkcolor [list pressed $colors(-darker)] \
							;
						# --------------------------------------------------
						# TCheckbutton and TRadiobutton
						# --------------------------------------------------
						ttk::style configure TCheckbutton \
							-indicatorbackground "#ffffff" \
							-indicatormargin {1 1 4 1} \
							-padding 2 ;
						ttk::style configure TRadiobutton \
							-indicatorbackground "#ffffff" \
							-indicatormargin {1 1 4 1} \
							-padding 2 ;
						ttk::style map TCheckbutton -indicatorbackground \
							[list  pressed $colors(-bgcolor) \
							{!disabled alternate} $colors(-alternate) \
							{disabled alternate} $colors(-darker) \
							disabled $colors(-disabledcolor)] \
							-background [list disabled $colors(-disabledcolor)]
						ttk::style map TRadiobutton -indicatorbackground \
							[list  pressed $colors(-bgcolor) \
							{!disabled alternate} $colors(-alternate) \
							{disabled alternate} $colors(-frame) \
							disabled $colors(-disabledcolor)] \
							-background [list disabled $colors(-disabledcolor)]
						# --------------------------------------------------
						# TMenubutton  (for future compatibility)
						# --------------------------------------------------
						ttk::style configure TMenubutton \
							-width -11 -padding 5 -relief raised
						# --------------------------------------------------
						# TEntry
						# --------------------------------------------------
						ttk::style configure TEntry -foreground $colors(-fgcolor) \
							-fieldbackground $colors(-tvwindow) -padding 1 -insertwidth 1
						ttk::style map TEntry \
							-background [list  readonly $colors(-frame)] \
							-foreground [list  readonly $colors(-fgcolor) \
							!disabled $colors(-fgcolor) \
							disabled $colors(-fgcolor)] \
							-fieldbackground [list !disabled $colors(-tvwindow) \
							disabled $colors(-tvwindowdisabled)] \
							-selectbackground [list !disabled $colors(-fieldfgcolor) \
							disabled $colors(-tvwindow)] \
							-selectforeground [list !disabled $colors(-fgcolor)] \
							-bordercolor [list  focus $colors(-selectbg)] \
							-lightcolor [list  focus "#6f9dc6"] \
							-darkcolor [list  focus "#6f9dc6"] \
							;

						# --------------------------------------------------
						# TCombobox
						# --------------------------------------------------
						ttk::style configure TCombobox -padding 1 -insertwidth 1
						ttk::style map TCombobox \
							-background [list active $colors(-bgcolor) pressed $colors(-lighter)] \
							-fieldbackground [list {readonly focus} $colors(-selectbackground) \
							readonly $colors(-frame) {!disabled} $colors(-tvwindow)] \
							-selectbackground [list !disabled $colors(-fieldfgcolor)] \
							-selectforeground [list !disabled $colors(-frame)] \
							-foreground [list {readonly focus} $colors(-selectforeground)] \
							-arrowcolor [list disabled $colors(-disabledfg)]

						ttk::style configure ComboboxPopdownFrame \
							-relief solid -borderwidth 1

						option add *TCombobox*Listbox.background $colors(-bgcolor)
						option add *TCombobox*Listbox.foreground $colors(-fgcolor)
						option add *TCombobox*Listbox.selectBackground $colors(-fieldfgcolor)
						# option add *TCombobox*Listbox.selectForeground $colors(-selectforeground)
                        # option add *TCombobox*Listbox.font font
						# --------------------------------------------------
						# TSpinbox
						# --------------------------------------------------
						ttk::style configure TSpinbox -arrowsize 10 -padding {2 0 10 0} \
							-background [list readonly $colors(-bgcolor)] \
							-foreground $colors(-fgcolor) \
							-fieldbackground $colors(-tvwindow) \
							-fieldforeground $colors(-fieldfgcolor) \
							-selectbackground springgreen \
							-selectforeground $colors(-fgcolor)
						ttk::style map TSpinbox \
							-background [list  readonly $colors(-frame) \
							!disabled $colors(-bgcolor) \
							disabled $colors(-bgcolor)] \
							-arrowcolor [list disabled $colors(-disabledfg)]

						# --------------------------------------------------
						# TNotebook
						# --------------------------------------------------
						ttk::style configure TNotebook.Tab -padding {6 2 6 2} -expand {0 0 2}
						ttk::style map TNotebook.Tab \
							-padding [list selected {6 4 6 2}] \
							-background [list selected gray54 active gray86 \
							!active lightgoldenrod3 {} $colors(-darker)] \
							-foreground [list selected white active black !active black] \
							-lightcolor [list selected $colors(-lighter) {} $colors(-dark)] \
							;
						ttk::style configure TabTopRight.TNotebook -tabposition "ne"
						ttk::style configure TabTopLeft.TNotebook -tabposition "nw"
						ttk::style configure TabTopCenter.TNotebook -tabposition "n"
						ttk::style configure TabRightTop.TNotebook -tabposition "en"
						ttk::style configure TabRightCenter.TNotebook -tabposition "e"
						ttk::style configure TabRightBottom.TNotebook -tabposition "es"
						ttk::style configure TabBottomLeft.TNotebook -tabposition "sw"
						ttk::style configure TabBottomCenter.TNotebook -tabposition "s"
						ttk::style configure TabBottomRight.TNotebook -tabposition "se"
						ttk::style configure TabLeftTop.TNotebook -tabposition "wn"
						ttk::style configure TabLeftCenter.TNotebook -tabposition "w"
						ttk::style configure TabLeftBottom.TNotebook -tabposition "ws"

						# --------------------------------------------------
						# Treeview:
						# --------------------------------------------------
						ttk::style configure Heading \
							-font TkHeadingFont -relief raised -padding {3}
						ttk::style configure Treeview -background $colors(-window)
						ttk::style map Treeview \
							-background [list disabled $colors(-frame)\
							selected $colors(-selectbg)] \
							-foreground [list disabled $colors(-disabledfg) \
							selected $colors(-selectfg)]

						# --------------------------------------------------
						# TFrame
						# --------------------------------------------------
						ttk::style configure TFrame \
							-background $colors(-bgcolor) -borderwidth 2 -relief groove
						ttk::style configure Flat.TFrame -relief flat -borderwidth 5
						ttk::style configure Sunken.TFrame -relief sunken -borderwidth 5
						# --------------------------------------------------
						# TLabelframe
						# --------------------------------------------------
						ttk::style configure TLabelframe \
							-background $colors(-bgcolor) -bordercolor $colors(-frame) \
							-labeloutside false -labelmargins {0 0 0 4} \
							-borderwidth 3 -relief groove
						ttk::style configure TLabelframe.Label -background $colors(-bgcolor)\
							-foreground $colors(-fgcolor) -padding {12 6}

						# --------------------------------------------------
						# TProgressbar
						# --------------------------------------------------
						ttk::style configure TProgressbar -background $colors(-bgcolor) \
							-troughcolor $colors(-troughcolor) -bordercolor $colors(-bordercolor) \
							-lightcolor $colors(-lightcolor) -darkcolor $colors(-barcolor)

						# --------------------------------------------------
						# TPanedwindow
						# --------------------------------------------------
						ttk::style configure TPanedwindow -background $colors(-bgcolor)
						ttk::style configure Sash -background $colors(-bgcolor) \
							-bordercolor $colors(-bordercolor) -sashthickness 8 -gripcount 10
					}
				}
				## END OF THEME FILE
