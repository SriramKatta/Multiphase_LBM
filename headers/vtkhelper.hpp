#pragma once
#include <string>
#include <fstream>

#include "lbmgrid.cuh"
#include "thrust/host_vector.h"

void vtkWriter(std::string fileOut, int &nx, int &ny, const thrust::host_vector<D2Q9::lattice> &grid)
{
    // Writing data from the vtk files
    int i, j;
    int N = nx * ny;
    std::ofstream vtkOut;
    vtkOut.open("./executable/output/" + fileOut  + ".vtk");
    vtkOut << "# vtk DataFile Version 4.0\nSiWiRVisFile\nASCII\nDATASET STRUCTURED_POINTS\n";
    vtkOut << "DIMENSIONS " << nx << " " << ny << " 1" << "\nORIGIN 0 0 0" << "\nSPACING 1 1 1" << "\nPOINT_DATA " << N;

    vtkOut << "\n\nSCALARS flags int 1\nLOOKUP_TABLE default\n";
    for (j = 0; j < ny ; ++j)
    {
        for (i = 0; i < nx ; ++i)
        {
            vtkOut <<  grid[TO1D(j ,i, nx, ny)].flag << "\n";
        }
    }
    vtkOut << "\n\nSCALARS density double 1\nLOOKUP_TABLE default\n";
    for (j = 0; j < ny; ++j)
    {
        for (i = 0; i < nx; ++i)
        {
            vtkOut << grid[TO1D(j ,i, nx, ny)].density << "\n";
        }
    }
    vtkOut << "\n\nVECTORS velocity double\n";
    for (j = 0; j < ny; ++j)
    {
        for (i = 0; i < nx; ++i)
        {
            vtkOut << grid[TO1D(j ,i, nx, ny)].u << " " << grid[TO1D(j ,i, nx, ny)].v << " 0\n";
        }
    }
    vtkOut.close();
    std::cout << "Data written to " << fileOut + ".vtk" << std::endl;
}
