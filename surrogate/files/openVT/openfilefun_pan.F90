!**********************************************************
!*********       Openfilefun_pan.F90              *********
!**********************************************************
!**                                                      **
!**  Open_mapInfo()                                      **
!**  Open_map()                                          **
!**                                                      **
!**  Open_hisInfo()                                      **
!**  Open_ncnetInfo()                                    **
!**  Open_ncgeomInfo()                                   **
!**  OpenBitmap()                                        **
!**                                                      **
!**********************************************************

!==========================================================
!=================     Open_mapInfo()    ==================
!==========================================================
subroutine Open_mapInfo()
use ifport
use VarGlob
use texture_test_sdiGlobals

Implicit None

character(len=40)                  :: moname(4)

real  :: nt
integer(4)  :: io_err
integer(4)  :: i

integer(8)  :: statarray(12)
integer(4)  :: istat

TYPE (T_RECT)  lpRect
!============================

    if (loadmapInfo) deallocate(MapValNameList)

    open (mapfID, file = trim(openfilename), form = 'binary',&
        status='old', IOSTAT = io_err)

    if (io_err == 0) then
        read (mapfID) moname
        read (mapfID) notot_map, noseg_map
        
        allocate(MapValNameList(notot_map))
    
        do i=1,notot_map
            read (mapfID) MapValNameList(i)
        end do
        
        istat = fstat(mapfID, statarray)
        nt = real(statarray(8)  &
             -4*40          &
             -2*4           &
             -notot_map*20) &
            /real(4+4*notot_map*noseg_map)
        ntime = int(nt)
                            
!        logicalt = UpdateWindow(ghwndMain)
    
        close(mapfID)
    end if
    
return
end subroutine Open_mapInfo

!==========================================================
!=================       Open_map()      ==================
!==========================================================
subroutine Open_map()
use iflogm

use VarGlob
use texture_test_sdiGlobals

Implicit None

include 'resource.fd'

character(len=40)                  :: moname(4)
character(len=20), allocatable   :: duname(:)

integer(kind=4)  :: i, j, k

type(DIALOG)  :: dlg_movie,dlg_loadmap

character(12)  :: testchar
!===========================
!            original
!            allocate(tempValMap(notot_map, noseg_map))
!            allocate(valmap(ntime,noseg_map,nresult))
        
!            test => invalidate memory
!            allocate(tempValMap(ntime,notot_map, noseg_map))
!            allocate(valmap(ntime,noseg_map,nresult))
!==========================================================   
if (loadini) then    
    allocate(valmap(ntime,noseg_map,nresult))            
    allocate(tempValMap(notot_map, noseg_map))

    do j=1,nresult
        iseg(j)=nullint
        
        do i=1,notot_map
            if (trim(MapValName(j)) .eq. trim(MapValNameList(i))) iseg(j) = i
        end do
    end do

    do k=1,ntime
        read (mapfID) maptime
        read (mapfID) ((tempValMap(i,j),i=1,notot_map),j=1,noseg_map)
        do j=1,nresult
        valmap(k,:,j) = tempValMap(iseg(j),1:noseg_map)
        end do
        logicalt = dlgSet(dlg_loadmap,IDC_PROGRESS_loadmap,k)
    end do
end if


end subroutine Open_map
