from django.test import TestCase
from test_count.models import *
from django.db.models import Count, Q
from django.db.utils import ProgrammingError

# Create your tests here.


class TestCountExtraArg(TestCase):

    def test_count_arg(self):
        t = Ticket.objects.create(heading="a")
        c1 = Commit.objects.create(ticket=t, message="a")
        c2 = Commit.objects.create(ticket=t, message="b")
        c3 = Commit.objects.create(ticket=t, message="c")
        queryset = Ticket.objects.filter(is_deleted=False)\
            .annotate(commit_count=Count('commit_set', filter=Q(is_deleted=False)))
        filtered_queryset = queryset.filter(heading__icontains='')
        result = queryset.filter(id__in=filtered_queryset.values('id'))
        len(result)
        self.assertEqual(result[0].commit_count, 3, result)
