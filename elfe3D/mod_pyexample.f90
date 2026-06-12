module pyexample

  implicit none

contains

subroutine add(A, B, C)

  real(kind=dp), dimension(:,:), intent(in) :: A, B
  real(kind=dp), allocatable, intent(out)   :: C(:,:)

  allocate(C(size(A, 1), size(A, 2)))

  C = A + B

end subroutine add


end module pyexample