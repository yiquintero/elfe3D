import numpy as np
import elfe3d

def main():
    
    #print("Launching Fortran elfe3d solver...")
    #elfe3d.solve() # This executes your Fortran 'subroutine solve'
    #print("Solver finished successfully!")

    # Use oder=F to match Fortran row-major memory layout
    A = np.array([[1.0, 2.0, 3.0],
                  [4.0, 5.0, 6.0], 
                  [7.0, 8.0, 9.0]], dtype=np.float64, order='F')

    B = np.array([[10.0, 20.0, 30.0],
                  [40.0, 50.0, 60.0], 
                  [70.0, 80.0, 90.0]], dtype=np.float64, order='F')

    # Call the module.sub-module.subroutine
    C = elfe3d.pyexample.add(A, B)

    print(C)

if __name__ == "__main__":
    main()