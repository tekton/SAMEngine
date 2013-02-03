# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'BattleBase'
        db.create_table('battles_battlebase', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('user_one', self.gf('django.db.models.fields.related.ForeignKey')(related_name='Player_One', to=orm['auth.User'])),
            ('user_two', self.gf('django.db.models.fields.related.ForeignKey')(related_name='Player_Two', to=orm['auth.User'])),
            ('battle_active', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('current_player_turn', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('winner', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('user_winner', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='Winner', null=True, to=orm['auth.User'])),
        ))
        db.send_create_signal('battles', ['BattleBase'])

        # Adding model 'ArmyComposition'
        db.create_table('battles_armycomposition', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('battle', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['battles.BattleBase'])),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('character_base', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['characters.BaseCharacter'])),
            ('redis_character_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal('battles', ['ArmyComposition'])


    def backwards(self, orm):
        # Deleting model 'BattleBase'
        db.delete_table('battles_battlebase')

        # Deleting model 'ArmyComposition'
        db.delete_table('battles_armycomposition')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'battles.armycomposition': {
            'Meta': {'object_name': 'ArmyComposition'},
            'battle': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['battles.BattleBase']"}),
            'character_base': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['characters.BaseCharacter']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'redis_character_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'battles.battlebase': {
            'Meta': {'object_name': 'BattleBase'},
            'battle_active': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'current_player_turn': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'user_one': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'Player_One'", 'to': "orm['auth.User']"}),
            'user_two': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'Player_Two'", 'to': "orm['auth.User']"}),
            'user_winner': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'Winner'", 'null': 'True', 'to': "orm['auth.User']"}),
            'winner': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'})
        },
        'characters.basecharacter': {
            'Meta': {'object_name': 'BaseCharacter'},
            'agility': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'essence': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'free_experience': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mind': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'spent_experience': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'strength': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'total_experience': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'visibility': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['battles']