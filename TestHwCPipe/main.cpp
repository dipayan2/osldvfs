#include<iostream>
// #include "HWCPipe/hwcpipe.h"
#include </Applications/Unity/Hub/Editor/2021.3.15f1/Unity.app/Contents/PluginAPI/IUnityInterface.h>
#include </Applications/Unity/Hub/Editor/2021.3.15f1/Unity.app/Contents/PluginAPI/IUnityProfiler.h>
#include </Applications/Unity/Hub/Editor/2021.3.15f1/Unity.app/Contents/PluginAPI/IUnityProfilerCallbacks.h>

// using namespace hwcpipe;


static IUnityProfiler* s_UnityProfiler = NULL;
static const UnityProfilerMarkerDesc* s_MyPluginMarker = NULL;
static bool s_IsDevelopmentBuild = false;

static void MyPluginWorkMethod()
{
    if (s_IsDevelopmentBuild)
        s_UnityProfiler->BeginSample(s_MyPluginMarker);

    // Code I want to see in Unity Profiler as "MyPluginMethod".
    // ...

    if (s_IsDevelopmentBuild)
        s_UnityProfiler->EndSample(s_MyPluginMarker);
}

extern "C" void UNITY_INTERFACE_EXPORT UNITY_INTERFACE_API UnityPluginLoad(IUnityInterfaces* unityInterfaces)
{
    s_UnityProfiler = unityInterfaces->Get<IUnityProfiler>();
    if (s_UnityProfiler == NULL)
        return;
    s_IsDevelopmentBuild = s_UnityProfiler->IsAvailable() != 0;
    s_UnityProfiler->CreateMarker(&s_MyPluginMarker, "MyPluginMethod", kUnityProfilerCategoryOther, kUnityProfilerMarkerFlagDefault, 0);
}

extern "C" void UNITY_INTERFACE_EXPORT UNITY_INTERFACE_API UnityPluginUnload()
{
    s_UnityProfiler  = NULL;
}

int main(int argc, char* argv[]){
    // HWCPipe h;

    IUnityInterface interface;
    
    // MyPluginWorkMethod();
    // s_UnityProfiler.
    
    printf("hello world\n");

    return 0;
}