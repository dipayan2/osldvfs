#include "ols_scheduler.h"

/**
 * Creates an OlsScheduler object containing a cpu_id_ of set_cpu_id,
 * a CpuClock with a cpu_id_ of set_cpu_id, a gpu_id_ of set_gpu_id
 * (even though GpuClock has no gpu_id_ member variable), a polling_time_
 * of set_polling_time, a GpuClock and a MemClock created with the default
 * constructors, and a a cluster_ of cluster
 * 
 * @param set_cpu_id       Set cpu_id_ to this value.
 *     Also makes cpu_man_ have this value as its cpu_id_.
 * @param set_gpu_id       Set gpu_id_ to this value.
 * @param set_polling_time Set polling_time_ to this value.
 * @param set_cluster      Set cluster_ to this value.
 *
 */
OlsScheduler::OlsScheduler(int set_cpu_id, int set_gpu_id, int set_polling_time, governor_settings set_cluster)
    : cpu_man_(set_cpu_id) {
    
    this->cpu_id_       = set_cpu_id;
    this->gpu_id_       = set_gpu_id;
    this->polling_time_ = set_polling_time;
    this->cluster_      = set_cluster;
}