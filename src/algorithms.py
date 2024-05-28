"""
This module contains the scheduling algorithms used in the scheduling API.

It provides implementations for both Least Deadline First (LDF) and Earliest Deadline First (EDF) scheduling strategies, applicable in single-core and multi-core processor environments. Functions within are designed to be called with specific application and platform data structures.

Functions:
- ldf_singlecore: Schedules tasks on a single-core processor using LDF.
- edf_singlecore: Schedules tasks on a single-core processor using EDF.
- rms_singlecore: Schedules tasks on a single-core processor using RMS.
- ll_singlecore: Schedules tasks on a single-core processor using LL.
- ldf_multicore: Schedules tasks on multiple cores using LDF.
- edf_multicore: Schedules tasks on multiple cores using EDF.
"""

__author__ = "Priya Nagar"
__version__ = "1.0.0"


import networkx as nx

# just an eample for the structure of the schedule to be returned and to check the frontend and backend connection
example_schedule = [
    {
        "job_id": "3",
        "node_id": 0,
        "end_time": 20,
        "deadline": 256,
        "start_time": 0,
    },
    {
        "job_id": "2",
        "node_id": 0,
        "end_time": 40,
        "deadline": 300,
        "start_time": 20,
    },
    {
        "job_id": "1",
        "node_id": 0,
        "end_time": 60,
        "deadline": 250,
        "start_time": 40,
    },
    {
        "job_id": "0",
        "node_id": 0,
        "end_time": 80,
        "deadline": 250,
        "start_time": 60,
    },
]


def ldf_singlecore(application_data):
    """
    Schedule jobs on a single core using the Latest Deadline First (LDF) strategy.

    Similar to the multi-core version but optimized for a single core, this function schedules jobs based on
    their latest deadlines after sorting them and considering dependencies through a directed graph representation.

    .. todo:: Implement Latest Dealine First Scheduling (LDF) algorithm.


    Args:
        application_data (dict): Contains jobs and messages that indicate dependencies among jobs.

    Returns:
        list of dict: Scheduling results with each job's details, including execution time, node assignment,
                      and start/end times relative to other jobs.
    """

    return {"schedule": example_schedule}


def edf_singlecore(application_data):
    """
    Schedule jobs on multiple cores using the Earliest Deadline First (EDF) strategy.

    This function processes application and platform data to organize and schedule jobs based on the earliest
    deadlines. It builds a dependency graph and schedules accordingly, ensuring that jobs with no predecessors are
    scheduled first, and subsequent jobs are scheduled based on the minimum deadline of available nodes.

    .. todo:: Implement Earliest Deadline First Scheduling (EDF) algorithm.

    Args:
        application_data (dict): Job data including dependencies represented by messages between jobs.

    Returns:
        list of dict: Contains the scheduled job details, each entry detailing the node assigned, start and end times,
                      and the job's deadline.
    """

    return {"schedule": example_schedule}


def rms_singlecore(application_data):
    """
    Schedule jobs on a single core using the Rate Monotonic Scheduling (RMS) strategy.
    This function schedules jobs based on their periods and deadlines, with the shortest period job being scheduled first.

    .. todo:: Implement Rate Monotonic Scheduling (RMS) algorithm.

    Args:
        application_data (dict): Job data including dependencies represented by messages between jobs.

    Returns:
        list of dict: Contains the scheduled job details, each entry detailing the node assigned, start and end times,
                      and the job's deadline.

    """
    return {"schedule": example_schedule}


def ll_singlecore(application_data):
    """
    Schedule jobs on a single core using the Least Laxity (LL) strategy.
    This function schedules jobs based on their laxity, with the job having the least laxity being scheduled first.

    .. todo:: Implement Least Laxity (LL) algorithm.

    Args:
        application_data (dict): Job data including dependencies represented by messages between jobs.

    Returns:
        list of dict: Contains the scheduled job details, each entry detailing the node assigned, start and end times,
                      and the job's deadline.

    """
    return {"schedule": example_schedule}
