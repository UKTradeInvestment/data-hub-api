from django.db.models import Count

from migrator.tests.models import SimpleObj
from migrator.tests.base import BaseMockedCDMSRestApiTestCase

from reversion.models import Revision, Version


class SingleObjMixin(object):
    def setUp(self):
        super(SingleObjMixin, self).setUp()
        self.obj = SimpleObj.objects.skip_cdms().create(
            cdms_pk='cdms-pk', name='name'
        )
        self.reset_revisions()


class AnnotateTestCase(BaseMockedCDMSRestApiTestCase):
    def test(self):
        self.assertRaises(
            NotImplementedError,
            SimpleObj.objects.annotate, Count('name')
        )
        self.assertNoAPICalled()
        self.assertNoRevisions()

    def test_skip_cdms(self):
        list(SimpleObj.objects.skip_cdms().annotate(Count('name')))
        self.assertNoAPICalled()
        self.assertNoRevisions()


class ReverseTestCase(BaseMockedCDMSRestApiTestCase):
    def test(self):
        self.assertRaises(
            NotImplementedError,
            SimpleObj.objects.reverse
        )
        self.assertNoAPICalled()
        self.assertNoRevisions()

    def test_skip_cdms(self):
        list(SimpleObj.objects.skip_cdms().reverse())
        self.assertNoAPICalled()
        self.assertNoRevisions()


class DistinctTestCase(BaseMockedCDMSRestApiTestCase):
    def test(self):
        self.assertRaises(
            NotImplementedError,
            SimpleObj.objects.distinct
        )
        self.assertNoAPICalled()
        self.assertNoRevisions()

    def test_skip_cdms(self):
        list(SimpleObj.objects.skip_cdms().distinct())
        self.assertNoAPICalled()
        self.assertNoRevisions()


class ValuesTestCase(BaseMockedCDMSRestApiTestCase):
    def test(self):
        self.assertRaises(
            NotImplementedError,
            SimpleObj.objects.values
        )
        self.assertNoAPICalled()
        self.assertNoRevisions()

    def test_skip_cdms(self):
        list(SimpleObj.objects.skip_cdms().values())
        self.assertNoAPICalled()
        self.assertNoRevisions()


class ValuesListTestCase(BaseMockedCDMSRestApiTestCase):
    def test(self):
        self.assertRaises(
            NotImplementedError,
            SimpleObj.objects.values_list
        )
        self.assertNoAPICalled()
        self.assertNoRevisions()

    def test_skip_cdms(self):
        list(SimpleObj.objects.skip_cdms().values_list())
        self.assertNoAPICalled()
        self.assertNoRevisions()


class DatesTestCase(BaseMockedCDMSRestApiTestCase):
    def test(self):
        self.assertRaises(
            NotImplementedError,
            SimpleObj.objects.dates, 'd_field', 'year'
        )
        self.assertNoAPICalled()
        self.assertNoRevisions()

    def test_skip_cdms(self):
        list(SimpleObj.objects.skip_cdms().dates('d_field', 'year'))
        self.assertNoAPICalled()
        self.assertNoRevisions()


class DatetimesTestCase(BaseMockedCDMSRestApiTestCase):
    def test(self):
        self.assertRaises(
            NotImplementedError,
            SimpleObj.objects.datetimes, 'd_field', 'year'
        )
        self.assertNoAPICalled()
        self.assertNoRevisions()

    def test_skip_cdms(self):
        list(SimpleObj.objects.skip_cdms().datetimes('dt_field', 'year'))
        self.assertNoAPICalled()
        self.assertNoRevisions()


class NoneTestCase(BaseMockedCDMSRestApiTestCase):
    def test(self):
        ret = list(SimpleObj.objects.none())
        self.assertEqual(ret, [])
        self.assertNoAPICalled()
        self.assertNoRevisions()

    def test_skip_cdms(self):
        list(SimpleObj.objects.skip_cdms().none())
        self.assertNoAPICalled()
        self.assertNoRevisions()


class SelectRelatedTestCase(SingleObjMixin, BaseMockedCDMSRestApiTestCase):
    def test(self):
        self.assertRaises(
            NotImplementedError,
            SimpleObj.objects.select_related
        )
        self.assertNoAPICalled()
        self.assertNoRevisions()

    def test_skip_cdms(self):
        SimpleObj.objects.skip_cdms().select_related('fk_obj').get(pk=self.obj.pk)
        self.assertNoAPICalled()
        self.assertNoRevisions()


class PrefetchRelatedTestCase(SingleObjMixin, BaseMockedCDMSRestApiTestCase):
    def test(self):
        self.assertRaises(
            NotImplementedError,
            SimpleObj.objects.prefetch_related
        )
        self.assertNoAPICalled()
        self.assertNoRevisions()

    def test_skip_cdms(self):
        self.assertRaises(
            NotImplementedError,
            SimpleObj.objects.skip_cdms().prefetch_related
        )
        self.assertNoAPICalled()
        self.assertNoRevisions()


class ExtraTestCase(BaseMockedCDMSRestApiTestCase):
    def test(self):
        self.assertRaises(
            NotImplementedError,
            SimpleObj.objects.extra, select={'is_recent': "dt_field > '2006-01-01'"}
        )
        self.assertNoAPICalled()
        self.assertNoRevisions()

    def test_skip_cdms(self):
        list(SimpleObj.objects.skip_cdms().extra(select={'is_recent': "dt_field > '2006-01-01'"}))
        self.assertNoAPICalled()
        self.assertNoRevisions()


class DeferTestCase(BaseMockedCDMSRestApiTestCase):
    def test(self):
        self.assertRaises(
            NotImplementedError,
            SimpleObj.objects.defer, 'name'
        )
        self.assertNoAPICalled()
        self.assertNoRevisions()

    def test_skip_cdms(self):
        list(SimpleObj.objects.skip_cdms().defer('name'))
        self.assertNoAPICalled()
        self.assertNoRevisions()


class OnlyTestCase(BaseMockedCDMSRestApiTestCase):
    def test(self):
        self.assertRaises(
            NotImplementedError,
            SimpleObj.objects.only, 'name'
        )
        self.assertNoAPICalled()
        self.assertNoRevisions()

    def test_skip_cdms(self):
        list(SimpleObj.objects.skip_cdms().only('name'))
        self.assertNoAPICalled()
        self.assertNoRevisions()


class RawTestCase(BaseMockedCDMSRestApiTestCase):
    def test(self):
        self.assertRaises(
            NotImplementedError,
            SimpleObj.objects.raw, 'select * from tests_simpleobj'
        )
        self.assertNoAPICalled()
        self.assertNoRevisions()

    def test_skip_cdms(self):
        list(SimpleObj.objects.skip_cdms().raw('select * from tests_simpleobj'))
        self.assertNoAPICalled()
        self.assertNoRevisions()


class GetOrCreateTestCase(BaseMockedCDMSRestApiTestCase):
    def test(self):
        self.assertRaises(
            NotImplementedError,
            SimpleObj.objects.get_or_create, name='name', defaults={'int_field': 1}
        )
        self.assertNoAPICalled()
        self.assertNoRevisions()

    def test_skip_cdms(self):
        SimpleObj.objects.skip_cdms().get_or_create(name='name', defaults={'int_field': 1})
        self.assertNoAPICalled()

        # check versions
        self.assertEqual(Version.objects.count(), 1)
        self.assertEqual(Revision.objects.count(), 1)


class UpdateOrCreateTestCase(BaseMockedCDMSRestApiTestCase):
    def test(self):
        self.assertRaises(
            NotImplementedError,
            SimpleObj.objects.update_or_create, name='name', defaults={'int_field': 1}
        )
        self.assertNoAPICalled()
        self.assertNoRevisions()

    def test_skip_cdms(self):
        SimpleObj.objects.skip_cdms().update_or_create(name='name', defaults={'int_field': 1})
        self.assertNoAPICalled()

        # check versions
        self.assertEqual(Version.objects.count(), 1)
        self.assertEqual(Revision.objects.count(), 1)


class CountTestCase(BaseMockedCDMSRestApiTestCase):
    def test(self):
        self.assertRaises(
            NotImplementedError,
            SimpleObj.objects.count
        )
        self.assertNoAPICalled()
        self.assertNoRevisions()

    def test_skip_cdms(self):
        SimpleObj.objects.skip_cdms().count()
        self.assertNoAPICalled()
        self.assertNoRevisions()


class InBulkTestCase(BaseMockedCDMSRestApiTestCase):
    def test(self):
        self.assertRaises(
            NotImplementedError,
            SimpleObj.objects.in_bulk, [1, 2]
        )
        self.assertNoAPICalled()
        self.assertNoRevisions()

    def test_skip_cdms(self):
        SimpleObj.objects.skip_cdms().in_bulk([1, 2])
        self.assertNoAPICalled()
        self.assertNoRevisions()


class LatestTestCase(SingleObjMixin, BaseMockedCDMSRestApiTestCase):
    def test(self):
        self.assertRaises(
            NotImplementedError,
            SimpleObj.objects.latest, 'dt_field'
        )
        self.assertNoAPICalled()
        self.assertNoRevisions()

    def test_skip_cdms(self):
        SimpleObj.objects.skip_cdms().latest('dt_field')
        self.assertNoAPICalled()
        self.assertNoRevisions()


class EarliestTestCase(SingleObjMixin, BaseMockedCDMSRestApiTestCase):
    def test(self):
        self.assertRaises(
            NotImplementedError,
            SimpleObj.objects.earliest, 'dt_field'
        )
        self.assertNoAPICalled()
        self.assertNoRevisions()

    def test_skip_cdms(self):
        SimpleObj.objects.skip_cdms().earliest('dt_field')
        self.assertNoAPICalled()
        self.assertNoRevisions()


class FirstTestCase(SingleObjMixin, BaseMockedCDMSRestApiTestCase):
    def test(self):
        self.assertRaises(
            NotImplementedError,
            SimpleObj.objects.first
        )
        self.assertNoAPICalled()
        self.assertNoRevisions()

    def test_skip_cdms(self):
        SimpleObj.objects.skip_cdms().first()
        self.assertNoAPICalled()
        self.assertNoRevisions()


class LastTestCase(SingleObjMixin, BaseMockedCDMSRestApiTestCase):
    def test(self):
        self.assertRaises(
            NotImplementedError,
            SimpleObj.objects.last
        )
        self.assertNoAPICalled()
        self.assertNoRevisions()

    def test_skip_cdms(self):
        SimpleObj.objects.skip_cdms().last()
        self.assertNoAPICalled()
        self.assertNoRevisions()


class AggregateTestCase(BaseMockedCDMSRestApiTestCase):
    def test(self):
        self.assertRaises(
            NotImplementedError,
            SimpleObj.objects.aggregate, Count('name')
        )
        self.assertNoAPICalled()
        self.assertNoRevisions()

    def test_skip_cdms(self):
        SimpleObj.objects.skip_cdms().aggregate(Count('name'))
        self.assertNoAPICalled()
        self.assertNoRevisions()


class ExistsTestCase(BaseMockedCDMSRestApiTestCase):
    def test(self):
        self.assertRaises(
            NotImplementedError,
            SimpleObj.objects.exists
        )
        self.assertNoAPICalled()

    def test_skip_cdms(self):
        SimpleObj.objects.skip_cdms().exists()
        self.assertNoAPICalled()
        self.assertNoRevisions()
