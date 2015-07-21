# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Members'
        db.create_table(u'main_members', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('logoff_ts', self.gf('django.db.models.fields.DateTimeField')()),
            ('join_ts', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'main', ['Members'])

        # Adding model 'Ships'
        db.create_table(u'main_ships', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'main', ['Ships'])

        # Adding model 'Location'
        db.create_table(u'main_location', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'main', ['Location'])


    def backwards(self, orm):
        # Deleting model 'Members'
        db.delete_table(u'main_members')

        # Deleting model 'Ships'
        db.delete_table(u'main_ships')

        # Deleting model 'Location'
        db.delete_table(u'main_location')


    models = {
        u'main.location': {
            'Meta': {'object_name': 'Location'},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'main.members': {
            'Meta': {'object_name': 'Members'},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'join_ts': ('django.db.models.fields.DateTimeField', [], {}),
            'logoff_ts': ('django.db.models.fields.DateTimeField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'main.ships': {
            'Meta': {'object_name': 'Ships'},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['main']