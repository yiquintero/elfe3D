import elfe3d

def main():
    print("Launching Fortran elfe3d solver...")
    
    # This executes your Fortran 'subroutine solve'
    elfe3d.solve()
    
    print("Solver finished successfully!")

if __name__ == "__main__":
    main()