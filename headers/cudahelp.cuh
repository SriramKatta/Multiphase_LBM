#pragma once
#include<tuple>

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