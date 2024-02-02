#include <stdio.h>
#include <stdlib.h>
struct edge
{
    int d;
    struct edge *link;
};
struct edge *create(int val)
{
    struct edge *ob = (struct edge *)malloc(sizeof(struct edge));
    ob->d = val;
    ob->link = NULL;
    return ob;
}
struct edge **adList(int vertices)
{
    int a;
    struct edge **list = (struct edge **)malloc(sizeof(struct edge) * vertices);
    for (int i = 0; i < vertices; ++i)
    {
        list[i] = create(i);
    }
    do
    {
        printf("Enter 1 for edge 2 to break : ");
        scanf("%d", &a);
        if (a == 1)
        {
            int s, d;
            printf("Enter Vertice 1 : ");
            scanf("%d", &s);
            printf("Enter Vertice 2 : ");
            scanf("%d",&d);
            struct edge *temp = list[s];
            while (temp->link != NULL)
            {
                temp = temp->link;
            }
            temp->link = create(d);
            temp = list[d];
            while (temp->link != NULL)
            {
                temp = temp->link;
            }
            temp->link = create(s);
        }
    } while (a != 2);
    for (int i = 0; i < vertices; ++i)
    {
        struct edge *temp = list[i];
        while (temp != NULL)
        {
            printf("%d ", temp->d);
            temp = temp->link;
        }
        printf("\n");
    }
    return list;
}
int **adMatrix(int vertices)
{
    int **mat = (int **)malloc(sizeof(int *) * vertices);
    for (int i = 0; i < vertices; ++i)
    {
        mat[i] = (int *)calloc(sizeof(int), vertices);
    }
    int a;
    do
    {
        printf("Enter 1 for edge 2 to break : ");
        scanf("%d", &a);
        if (a == 1)
        {
            printf("Enter Vertice 1 : ");
            int s, d;
            scanf("%d", &s);
            printf("Enter Vertice 2 : ");
            scanf("%d",&d);
            mat[s][d] = 1;
            mat[d][s] = 1;
        }
    } while (a != 2);
    for (int i = 0; i < vertices; ++i)
    {
        for (int j = 0; j < vertices; ++j)
        {
            printf("%d ", mat[i][j]);
        }
        printf("\n");
    }
    return mat;
}
void main()
{
    int v;
    printf("Enter no. of vertices : ");
    scanf("%d", &v);
    struct edge **list = adList(v);
    int **mat = adMatrix(v);
}