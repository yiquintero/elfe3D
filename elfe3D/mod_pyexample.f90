module pyexample

  use mod_constant

  implicit none

contains

subroutine add(A, B, C, m, n)
  integer, intent(in) :: m, n
  real(kind=dp), dimension(m, n), intent(in)  :: A, B
  real(kind=dp), dimension(m, n), intent(out) :: C

  C = A + B
end subroutine add


end module pyexample