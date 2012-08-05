!include "MUI2.nsh"

!define APPNAME "MMAnywhere"

# installer pages
#!insertmacro MUI_PAGE_WELCOME
!insertmacro MUI_PAGE_DIRECTORY
!insertmacro MUI_PAGE_INSTFILES
#!insertmacro MUI_PAGE_FINISH

# define name of installer
outFile "MMAnywhere-installer.exe"
 
# define installation directory
installDir "$PROGRAMFILES\${APPNAME}"
 
# start default section
section
 
    # set the installation directory as the destination for the following actions
    SetOutPath $INSTDIR
	
	File /r dist\*.*
 
    # create the uninstaller
    WriteUninstaller "$INSTDIR\uninstall.exe"
 
	CreateShortCut "$SMPROGRAMS\${APPNAME}\Run MMAnywhere.lnk" "$INSTDIR\mm_anywhere.exe"
	
    # point the new shortcut at the program uninstaller
    CreateShortCut "$SMPROGRAMS\${APPNAME}\Uninstall MMAnywhere.lnk" "$INSTDIR\uninstall.exe"
sectionEnd

# uninstaller pages 
#!insertmacro MUI_UNPAGE_WELCOME
!insertmacro MUI_UNPAGE_CONFIRM
!insertmacro MUI_UNPAGE_DIRECTORY
!insertmacro MUI_UNPAGE_INSTFILES
#!insertmacro MUI_UNPAGE_FINISH

# uninstaller section start
section "uninstall"

    # remove the link from the start menu
	Delete "$SMPROGRAMS\${APPNAME}\Uninstall MMAnywhere.lnk"
	RMDir /r "$SMPROGRAMS\${APPNAME}"
 
    # delete the uninstaller
    Delete "$INSTDIR\uninstall.exe"
	
	RMDir /r $INSTDIR
 
 
# uninstaller section end
sectionEnd