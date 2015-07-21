# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing unique constraint on 'Member', fields ['ship']
        db.delete_unique(u'main_member', ['ship_id'])

        # Removing unique constraint on 'Member', fields ['location']
        db.delete_unique(u'main_member', ['location_id'])


        # Changing field 'Member.location'
        db.alter_column(u'main_member', 'location_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Location'], null=True))

        # Changing field 'Member.ship'
        db.alter_column(u'main_member', 'ship_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Ship'], null=True))

    def backwards(self, orm):

        # Changing field 'Member.location'
        db.alter_column(u'main_member', 'location_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['main.Location'], unique=True, null=True))
        # Adding unique constraint on 'Member', fields ['location']
        db.create_unique(u'main_member', ['location_id'])


        # Changing field 'Member.ship'
        db.alter_column(u'main_member', 'ship_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['main.Ship'], unique=True, null=True))
        # Adding unique constraint on 'Member', fields ['ship']
        db.create_unique(u'main_member', ['ship_id'])


    models = {
        u'main.location': {
            'Meta': {'object_name': 'Location'},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'})
        },
        u'main.member': {
            'Meta': {'object_name': 'Member'},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'join_ts': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['main.Location']", 'null': 'True'}),
            'logoff_ts': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'ship': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['main.Ship']", 'null': 'True'})
        },
        u'main.ship': {
            'Meta': {'object_name': 'Ship'},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'})
        }
    }

    complete_apps = ['main']