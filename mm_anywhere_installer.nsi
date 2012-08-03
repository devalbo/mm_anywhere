# define name of installer
outFile "MMAnywhere-installer.exe"
 
# define installation directory
installDir "$PROGRAMFILES\MMAnywhere"
 
# start default section
section
 
    # set the installation directory as the destination for the following actions
    SetOutPath $INSTDIR
	
	File /r dist\*.*
 
    # create the uninstaller
    WriteUninstaller "$INSTDIR\uninstall.exe"
 
	CreateShortCut "$SMPROGRAMS\MMAnywhere\Run MMAnywhere.lnk" "$INSTDIR\mm_anywhere.exe"
	
    # point the new shortcut at the program uninstaller
    CreateShortCut "$SMPROGRAMS\MMAnywhere\Uninstall MMAnywhere.lnk" "$INSTDIR\uninstall.exe"
sectionEnd
 
# uninstaller section start
section "uninstall"

    # remove the link from the start menu
	Delete "$SMPROGRAMS\MMAnywhere\Uninstall MMAnywhere.lnk"
	RMDir /r "$SMPROGRAMS\MMAnywhere"
 
    # delete the uninstaller
    Delete "$INSTDIR\uninstall.exe"
	
	RMDir /r $INSTDIR
 
 
# uninstaller section end
sectionEnd