#include <stdio.h>
#include <stdlib.h>  // for system (to clear screen)
#include <pthread.h> // for multi-threading
#include <unistd.h>  // for sleep
#include <time.h>    // to get the current time

pthread_mutex_t mutex; // = PTHREAD_MUTEX_INITIALIZER;
int ss, mm, hh;

void *updateSeconds()
{
    // start critical section
    pthread_mutex_lock(&mutex);

    while (1)
    {
        ss++;
        if (ss == 60)
        {
            ss = 0;
            mm++;
        }

        system("clear");
        printf("%02d:%02d:%02d\n", hh, mm, ss);
        sleep(1);
    }

    // end critical section
    pthread_mutex_unlock(&mutex);

    pthread_exit(NULL);
}

void *updateMinutes()
{
    // start critical section
    pthread_mutex_lock(&mutex);

    while (1)
    {
        if (mm == 60)
        {
            mm = 0;
            hh++;
        }
    }

    // end critical section
    pthread_mutex_unlock(&mutex);

    pthread_exit(NULL);
}

void *updateHours()
{
    // start critical section
    pthread_mutex_lock(&mutex);

    while (1)
    {
        if (hh == 24)
            hh = 0;
    }

    // end critical section
    pthread_mutex_unlock(&mutex);

    pthread_exit(NULL);
}

int main()
{
    time_t now = time(NULL);
    struct tm *ltime = localtime(&now);

    ss = ltime->tm_sec;
    mm = ltime->tm_min;
    hh = ltime->tm_hour;

    pthread_mutex_init(&mutex, NULL);

    pthread_t id1;
    pthread_create(&id1, NULL, updateSeconds, NULL);
    pthread_t id2;
    pthread_create(&id2, NULL, updateMinutes, NULL);
    pthread_t id3;
    pthread_create(&id3, NULL, updateHours, NULL);

    // synchronize threads:
    pthread_join(id1, NULL);
    pthread_join(id2, NULL);
    pthread_join(id3, NULL);

    pthread_mutex_destroy(&mutex);
    return 0;
}
