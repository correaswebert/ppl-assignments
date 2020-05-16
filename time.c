#include <stdio.h>
#include <pthread.h>
#include <time.h>

pthread_mutex_t mutex; // = PTHREAD_MUTEX_INITIALIZER;

void *getTime(void *args)
{
    int hh = *(int *)args;

    // start critical section
    pthread_mutex_lock(&mutex);

    printf("%02d:", hh);

    // end critical section
    pthread_mutex_unlock(&mutex);

    pthread_exit(NULL);
}

int main()
{
    time_t now = time(NULL);
    struct tm *ltime = localtime(&now);

    pthread_mutex_init(&mutex, NULL);

    pthread_t id1;
    pthread_create(&id1, NULL, getTime, &ltime->tm_hour);
    pthread_t id2;
    pthread_create(&id2, NULL, getTime, &ltime->tm_min);
    pthread_t id3;
    pthread_create(&id3, NULL, getTime, &ltime->tm_sec);

    // synchronize threads:
    pthread_join(id1, NULL);
    pthread_join(id2, NULL);
    pthread_join(id3, NULL);

    return 0;
}
