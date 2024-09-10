#pragma once
#include <string>
#include <fstream>

#include "lbmgrid.cuh"
#include "thrust/host_vector.h"

void vtkWriter(std::string fileOut, int &nx, int &ny, const thrust::host_vector<lattice> &grid)
{
    // Writing data from the vtk files
    uint i, j;
    uint N = nx * ny;
    std::ofstream vtkOut;
    vtkOut.open("./results/" + fileOut + std::to_string(t) + ".vtk");
    vtkOut << "# vtk DataFile Version 4.0\nSiWiRVisFile\nASCII\nDATASET STRUCTURED_POINTS\n";
    vtkOut << "DIMENSIONS " << nx << " " << ny << " 1" << "\nORIGIN 0 0 0" << "\nSPACING 1 1 1" << "\nPOINT_DATA " << N;

    vtkOut << "\n\nSCALARS flags int 1\nLOOKUP_TABLE default\n";
    for (j = 1; j < ny + 1; ++j)
    {
        for (i = 1; i < nx + 1; ++i)
        {
            vtkOut << flag(i, j) << "\n";
        }
    }
    vtkOut << "\n\nSCALARS density double 1\nLOOKUP_TABLE default\n";
    for (j = 1; j < ny + 1; ++j)
    {
        for (i = 1; i < nx + 1; ++i)
        {
            vtkOut << density(i, j) << "\n";
        }
    }
    vtkOut << "\n\nVECTORS velocity double\n";
    for (j = 1; j < ny + 1; ++j)
    {
        for (i = 1; i < nx + 1; ++i)
        {
            vtkOut << u(i, j) << " " << v(i, j) << " 0\n";
        }
    }
    vtkOut.close();
    std::cout << "Data written to " << fileOut + std::to_string(t) + ".vtk" << std::endl;
}
