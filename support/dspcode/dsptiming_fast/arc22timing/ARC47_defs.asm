; ARC47_defs.asm
; 02Sep10 last change MPL

; *** define SXMIT based on selected channels ***
; ARC47 ADC conversion codes
;$00F000	BRD#0 A/D#0
;$00F041	BRD#0 A/D#1
;$00F082	BRD#0 A/D#2
;$00F0C3	BRD#0 A/D#3
;$00F104	BRD#0 A/D#4
;$00F145	BRD#0 A/D#5
;$00F186	BRD#0 A/D#6
;$00F1C7	BRD#0 A/D#7
;$00F208	BRD#1 A/D#0
;$00F249	BRD#1 A/D#1
;$00F28A	BRD#1 A/D#2
;$00F2CB	BRD#1 A/D#3
;$00F30C	BRD#1 A/D#4
;$00F34D	BRD#1 A/D#5
;$00F38E	BRD#1 A/D#6
;$00F3CF	BRD#1 A/D#7
;$00F1C0 	BRD#0 A/D#0-#7
;$00F3C8	BRD#1 A/D#0-#7
;$00F3C0	BRD#0-#1 A/D#0-#7

	IF	@SCP("CHANNELS","8A")
SXMIT	EQU	$00F1C0
	ENDIF
	IF	@SCP("CHANNELS","8B")
SXMIT	EQU	$00F3C8
	ENDIF
	IF	@SCP("CHANNELS","16")
SXMIT	EQU	$00F3C0
	ENDIF
	IF	@SCP("CHANNELS","32")
SXMIT	EQU	$00F7C0
	ENDIF
	IF	@SCP("CHANNELS","0")
SXMIT	EQU	$00F000
	ENDIF
	IF	@SCP("CHANNELS","1")
SXMIT	EQU	$00F041
	ENDIF
	IF	@SCP("CHANNELS","2")
SXMIT	EQU	$00F082
	ENDIF
	IF	@SCP("CHANNELS","3")
SXMIT	EQU	$00F0C3
	ENDIF
	IF	@SCP("CHANNELS","01")
SXMIT	EQU	$00F040
	ENDIF
	IF	@SCP("CHANNELS","23")
SXMIT	EQU	$00F0C2
	ENDIF
	IF	@SCP("CHANNELS","0123")
SXMIT	EQU	$00F0C0
	ENDIF

; timing
S_DELAY	EQU	@CVI((SERDEL-40)/40)<<16
R_DELAY	EQU	@CVI((RSTDEL-40)/40)<<16
;V_DELAY	EQU	@CVI((VIDDEL-40)/40)<<16
P_DELAY	EQU	@CVI((PARDEL-40)/40)<<16
DWELL	EQU	@CVI((SAMPLE-40)/40)<<16

; ARC47 gain : $0D000g, g = 0 to %1111, Gain = 1.00 to 4.75 in steps of 0.25
; 0	1.00		 8	3.00
; 1	1.25		 9	3.25	
; 2	1.50		10	3.75
; 3	1.75		11	4.00
; 4	2.00		12	4.25
; 5	2.25		13	4.50
; 6	2.50		14	4.75
; 7	2.75		15	forbidden?

; voltage to DN

VOD_MAX	 EQU	30.45
VRD_MAX	 EQU	19.90
VOG_MAX	 EQU	8.70
VRSV_MAX EQU	8.70

DAC_VOD1  EQU	@CVI((VOD1/VOD_MAX)*16384-1)		; Unipolar
DAC_VRD1  EQU	@CVI((VRD1/VRD_MAX)*16384-1)		; Unipolar
DAC_VOG1  EQU	@CVI(((VOG1+VOG_MAX)/VOG_MAX)*8192-1)	; Bipolar
DAC_VRSV1 EQU	@CVI(((VRSV1+VRSV_MAX)/VRSV_MAX)*8192-1) ; Bipolar

DAC_VOD2  EQU	@CVI((VOD2/VOD_MAX)*16384-1)		; Unipolar
DAC_VRD2  EQU	@CVI((VRD2/VRD_MAX)*16384-1)		; Unipolar
DAC_VOG2  EQU	@CVI(((VOG2+VOG_MAX)/VOG_MAX)*8192-1)	; Bipolar
DAC_VRSV2 EQU	@CVI(((VRSV2+VRSV_MAX)/VRSV_MAX)*8192-1) ; Bipolar

DAC_VOD3  EQU	@CVI((VOD3/VOD_MAX)*16384-1)		; Unipolar
DAC_VRD3  EQU	@CVI((VRD3/VRD_MAX)*16384-1)		; Unipolar
DAC_VOG3  EQU	@CVI(((VOG3+VOG_MAX)/VOG_MAX)*8192-1)	; Bipolar
DAC_VRSV3 EQU	@CVI(((VRSV3+VRSV_MAX)/VRSV_MAX)*8192-1) ; Bipolar

DAC_VOD4  EQU	@CVI((VOD4/VOD_MAX)*16384-1)		; Unipolar
DAC_VRD4  EQU	@CVI((VRD4/VRD_MAX)*16384-1)		; Unipolar
DAC_VOG4  EQU	@CVI(((VOG4+VOG_MAX)/VOG_MAX)*8192-1)	; Bipolar
DAC_VRSV4 EQU	@CVI(((VRSV4+VRSV_MAX)/VRSV_MAX)*8192-1) ; Bipolar

DAC_VOD5  EQU	@CVI((VOD5/VOD_MAX)*16384-1)		; Unipolar
DAC_VRD5  EQU	@CVI((VRD5/VRD_MAX)*16384-1)		; Unipolar
DAC_VOG5  EQU	@CVI(((VOG5+VOG_MAX)/VOG_MAX)*8192-1)	; Bipolar
DAC_VRSV5 EQU	@CVI(((VRSV5+VRSV_MAX)/VRSV_MAX)*8192-1) ; Bipolar

DAC_VOD6  EQU	@CVI((VOD6/VOD_MAX)*16384-1)		; Unipolar
DAC_VRD6  EQU	@CVI((VRD6/VRD_MAX)*16384-1)		; Unipolar
DAC_VOG6  EQU	@CVI(((VOG6+VOG_MAX)/VOG_MAX)*8192-1)	; Bipolar
DAC_VRSV6 EQU	@CVI(((VRSV6+VRSV_MAX)/VRSV_MAX)*8192-1) ; Bipolar

DAC_VOD7  EQU	@CVI((VOD7/VOD_MAX)*16384-1)		; Unipolar
DAC_VRD7  EQU	@CVI((VRD7/VRD_MAX)*16384-1)		; Unipolar
DAC_VOG7  EQU	@CVI(((VOG7+VOG_MAX)/VOG_MAX)*8192-1)	; Bipolar
DAC_VRSV7 EQU	@CVI(((VRSV7+VRSV_MAX)/VRSV_MAX)*8192-1) ; Bipolar

DAC_VOD8  EQU	@CVI((VOD8/VOD_MAX)*16384-1)		; Unipolar
DAC_VRD8  EQU	@CVI((VRD8/VRD_MAX)*16384-1)		; Unipolar
DAC_VOG8  EQU	@CVI(((VOG8+VOG_MAX)/VOG_MAX)*8192-1)	; Bipolar
DAC_VRSV8 EQU	@CVI(((VRSV8+VRSV_MAX)/VRSV_MAX)*8192-1) ; Bipolar

DAC_VOD9  EQU	@CVI((VOD9/VOD_MAX)*16384-1)		; Unipolar
DAC_VRD9  EQU	@CVI((VRD9/VRD_MAX)*16384-1)		; Unipolar
DAC_VOG9  EQU	@CVI(((VOG9+VOG_MAX)/VOG_MAX)*8192-1)	; Bipolar
DAC_VRSV9 EQU	@CVI(((VRSV9+VRSV_MAX)/VRSV_MAX)*8192-1) ; Bipolar

DAC_VOD10  EQU	@CVI((VOD10/VOD_MAX)*16384-1)		; Unipolar
DAC_VRD10  EQU	@CVI((VRD10/VRD_MAX)*16384-1)		; Unipolar
DAC_VOG10  EQU	@CVI(((VOG10+VOG_MAX)/VOG_MAX)*8192-1)	; Bipolar
DAC_VRSV10 EQU	@CVI(((VRSV10+VRSV_MAX)/VRSV_MAX)*8192-1) ; Bipolar

DAC_VOD11  EQU	@CVI((VOD11/VOD_MAX)*16384-1)		; Unipolar
DAC_VRD11  EQU	@CVI((VRD11/VRD_MAX)*16384-1)		; Unipolar
DAC_VOG11  EQU	@CVI(((VOG11+VOG_MAX)/VOG_MAX)*8192-1)	; Bipolar
DAC_VRSV11 EQU	@CVI(((VRSV11+VRSV_MAX)/VRSV_MAX)*8192-1) ; Bipolar

DAC_VOD12  EQU	@CVI((VOD12/VOD_MAX)*16384-1)		; Unipolar
DAC_VRD12  EQU	@CVI((VRD12/VRD_MAX)*16384-1)		; Unipolar
DAC_VOG12  EQU	@CVI(((VOG12+VOG_MAX)/VOG_MAX)*8192-1)	; Bipolar
DAC_VRSV12 EQU	@CVI(((VRSV12+VRSV_MAX)/VRSV_MAX)*8192-1) ; Bipolar

DAC_VOD13  EQU	@CVI((VOD13/VOD_MAX)*16384-1)		; Unipolar
DAC_VRD13  EQU	@CVI((VRD13/VRD_MAX)*16384-1)		; Unipolar
DAC_VOG13  EQU	@CVI(((VOG13+VOG_MAX)/VOG_MAX)*8192-1)	; Bipolar
DAC_VRSV13 EQU	@CVI(((VRSV13+VRSV_MAX)/VRSV_MAX)*8192-1) ; Bipolar

DAC_VOD14  EQU	@CVI((VOD14/VOD_MAX)*16384-1)		; Unipolar
DAC_VRD14  EQU	@CVI((VRD14/VRD_MAX)*16384-1)		; Unipolar
DAC_VOG14  EQU	@CVI(((VOG14+VOG_MAX)/VOG_MAX)*8192-1)	; Bipolar
DAC_VRSV14 EQU	@CVI(((VRSV14+VRSV_MAX)/VRSV_MAX)*8192-1) ; Bipolar

DAC_VOD15  EQU	@CVI((VOD15/VOD_MAX)*16384-1)		; Unipolar
DAC_VRD15  EQU	@CVI((VRD15/VRD_MAX)*16384-1)		; Unipolar
DAC_VOG15  EQU	@CVI(((VOG15+VOG_MAX)/VOG_MAX)*8192-1)	; Bipolar
DAC_VRSV15 EQU	@CVI(((VRSV15+VRSV_MAX)/VRSV_MAX)*8192-1) ; Bipolar

DAC_VOD16  EQU	@CVI((VOD16/VOD_MAX)*16384-1)		; Unipolar
DAC_VRD16  EQU	@CVI((VRD16/VRD_MAX)*16384-1)		; Unipolar
DAC_VOG16  EQU	@CVI(((VOG16+VOG_MAX)/VOG_MAX)*8192-1)	; Bipolar
DAC_VRSV16 EQU	@CVI(((VRSV16+VRSV_MAX)/VRSV_MAX)*8192-1) ; Bipolar

DAC_VSCP1  EQU	@CVI((VSCP1/VOD_MAX)*16384-1)		; Unipolar
DAC_VSCP2  EQU	@CVI((VSCP2/VOD_MAX)*16384-1)		; Unipolar
DAC_VSCP3  EQU	@CVI((VSCP3/VOD_MAX)*16384-1)		; Unipolar
DAC_VSCP4  EQU	@CVI((VSCP4/VOD_MAX)*16384-1)		; Unipolar

