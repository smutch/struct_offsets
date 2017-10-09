#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>
#include "{{ header }}"

int main()
{
    {% for member in members %}
    printf("{{ struct }}.{{ member }} = %lu\n", offsetof( {{ struct }}, {{ member }} ));
    {% endfor %}
    return 0;
}
