#pragma once
#include <tuple>

#define GRID_STRIDE_1D(index, stride)                  \
    int index = blockIdx.x * blockDim.x + threadIdx.x; \
    int stride = gridDim.x * blockDim.x;

#define GRID_STRIDE_2D(ix, stridex, iy, stridey)                      \
    int ix = blockIdx.x * blockDim.x + threadIdx.x; \
    int stridex = gridDim.x * blockDim.x;            \
    int iy = blockIdx.y * blockDim.y + threadIdx.y; \
    int stridey = gridDim.y * blockDim.y;

std::tuple<int, int> getgpuconfig(int warpMultiuple = 16, int blockMultiple = 10)
{
    int deviceId;
    int numberOfSMs;
    int warps;

    cudaGetDevice(&deviceId);
    cudaDeviceGetAttribute(&numberOfSMs, cudaDevAttrMultiProcessorCount, deviceId);
    cudaDeviceGetAttribute(&warps, cudaDevAttrWarpSize, deviceId);

    int threadspblk = warps * warpMultiuple;
    int blocks = numberOfSMs * blockMultiple;
    return {threadspblk, blocks};
}

std::tuple<dim3, dim3> getgpuconfig2D(int warpMultipleX = 5, int warpMultipleY = 5, int blockMultipleX = 5, int blockMultipleY = 5)
{
    int deviceId;
    int numberOfSMs;
    int warps;

    cudaGetDevice(&deviceId);
    cudaDeviceGetAttribute(&numberOfSMs, cudaDevAttrMultiProcessorCount, deviceId);
    cudaDeviceGetAttribute(&warps, cudaDevAttrWarpSize, deviceId);

    int threadsPerBlockX = warps * warpMultipleX;
    int threadsPerBlockY = warpMultipleY;
    
    int blocksX = numberOfSMs * blockMultipleX;
    int blocksY = blockMultipleY;

    dim3 thpblk(threadsPerBlockX, threadsPerBlockY);
    dim3 blks(blocksX, blocksY);

    return {thpblk, blks};
}
