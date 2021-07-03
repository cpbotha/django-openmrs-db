# OpenMRS 2.11+ models for Django
# this file is copyright Charl P. Botha <cpbotha@vxlabs.com> 2021
# plan is to release as open source

# this file was generated on top of an openmrs-qa (dev) ref app on 2021-06-26

# we set default_related_name = '+' on most models to get the system running
# https://docs.djangoproject.com/en/dev/ref/models/options/#django.db.models.Options.default_related_name
# and then started to set related_name better on the models that we were using

# we have also started impementing __str__() calls for the most important models
# so that they appear with usable names in the admin interface

# guidelines
# ==========
# - we would like to maintain backwards compatibility with true OpenMRS, so keep
#   db_table and db_column instances the same
# - as far as possible, keep field names the same for parity with the OpenMRS API

from django.db import models


class AddressHierarchyAddressToEntryMap(models.Model):
    address_to_entry_map_id = models.AutoField(primary_key=True)
    address = models.ForeignKey('PersonAddress', models.DO_NOTHING)
    entry = models.ForeignKey('AddressHierarchyEntry', models.DO_NOTHING)
    uuid = models.CharField(max_length=38)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'address_hierarchy_address_to_entry_map'


class AddressHierarchyEntry(models.Model):
    address_hierarchy_entry_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=160, blank=True, null=True)
    level = models.ForeignKey('AddressHierarchyLevel', models.DO_NOTHING)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    user_generated_id = models.CharField(max_length=11, blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    elevation = models.FloatField(blank=True, null=True)
    uuid = models.CharField(max_length=38)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'address_hierarchy_entry'


class AddressHierarchyLevel(models.Model):
    address_hierarchy_level_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=160, blank=True, null=True)
    parent_level = models.OneToOneField('self', models.DO_NOTHING, blank=True, null=True)
    address_field = models.CharField(max_length=50, blank=True, null=True)
    uuid = models.CharField(max_length=38)
    required = models.IntegerField()

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'address_hierarchy_level'


class Allergy(models.Model):
    allergy_id = models.AutoField(primary_key=True)
    patient = models.ForeignKey('Patient', models.DO_NOTHING)
    severity_concept = models.ForeignKey('Concept', models.DO_NOTHING, blank=True, null=True)
    coded_allergen = models.ForeignKey('Concept', models.DO_NOTHING, db_column='coded_allergen')
    non_coded_allergen = models.CharField(max_length=255, blank=True, null=True)
    allergen_type = models.CharField(max_length=50)
    comments = models.CharField(max_length=1024, blank=True, null=True)
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    voided = models.IntegerField()
    voided_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='voided_by', blank=True, null=True)
    date_voided = models.DateTimeField(blank=True, null=True)
    void_reason = models.CharField(max_length=255, blank=True, null=True)
    uuid = models.CharField(max_length=38, blank=True, null=True)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'allergy'


class AllergyReaction(models.Model):
    allergy_reaction_id = models.AutoField(primary_key=True)
    allergy = models.ForeignKey(Allergy, models.DO_NOTHING)
    reaction_concept = models.ForeignKey('Concept', models.DO_NOTHING)
    reaction_non_coded = models.CharField(max_length=255, blank=True, null=True)
    uuid = models.CharField(max_length=38, blank=True, null=True)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'allergy_reaction'


class AppframeworkComponentState(models.Model):
    component_state_id = models.AutoField(primary_key=True)
    uuid = models.CharField(max_length=38)
    component_id = models.CharField(max_length=255)
    component_type = models.CharField(max_length=50)
    enabled = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'appframework_component_state'


class AppframeworkUserApp(models.Model):
    app_id = models.CharField(primary_key=True, max_length=50)
    json = models.TextField()

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'appframework_user_app'


class AppointmentschedulingAppointment(models.Model):
    appointment_id = models.AutoField(primary_key=True)
    time_slot = models.ForeignKey('AppointmentschedulingTimeSlot', models.DO_NOTHING)
    visit = models.ForeignKey('Visit', models.DO_NOTHING, blank=True, null=True)
    patient = models.ForeignKey('Patient', models.DO_NOTHING)
    appointment_type = models.ForeignKey('AppointmentschedulingAppointmentType', models.DO_NOTHING)
    status = models.CharField(max_length=255)
    reason = models.CharField(max_length=1024, blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38)
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    voided = models.IntegerField()
    voided_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='voided_by', blank=True, null=True)
    date_voided = models.DateTimeField(blank=True, null=True)
    void_reason = models.CharField(max_length=255, blank=True, null=True)
    cancel_reason = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'appointmentscheduling_appointment'


class AppointmentschedulingAppointmentBlock(models.Model):
    appointment_block_id = models.AutoField(primary_key=True)
    location = models.ForeignKey('Location', models.DO_NOTHING)
    provider = models.ForeignKey('Provider', models.DO_NOTHING, blank=True, null=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    uuid = models.CharField(unique=True, max_length=38)
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    voided = models.IntegerField()
    voided_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='voided_by', blank=True, null=True)
    date_voided = models.DateTimeField(blank=True, null=True)
    void_reason = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'appointmentscheduling_appointment_block'


class AppointmentschedulingAppointmentRequest(models.Model):
    appointment_request_id = models.AutoField(primary_key=True)
    patient = models.ForeignKey('Patient', models.DO_NOTHING)
    appointment_type = models.ForeignKey('AppointmentschedulingAppointmentType', models.DO_NOTHING)
    status = models.CharField(max_length=255)
    provider = models.ForeignKey('Provider', models.DO_NOTHING, blank=True, null=True)
    requested_by = models.ForeignKey('Provider', models.DO_NOTHING, db_column='requested_by', blank=True, null=True)
    requested_on = models.DateTimeField()
    min_time_frame_value = models.IntegerField(blank=True, null=True)
    min_time_frame_units = models.CharField(max_length=255, blank=True, null=True)
    max_time_frame_value = models.IntegerField(blank=True, null=True)
    max_time_frame_units = models.CharField(max_length=255, blank=True, null=True)
    notes = models.CharField(max_length=1024, blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38)
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    voided = models.IntegerField()
    voided_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='voided_by', blank=True, null=True)
    date_voided = models.DateTimeField(blank=True, null=True)
    void_reason = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'appointmentscheduling_appointment_request'


class AppointmentschedulingAppointmentStatusHistory(models.Model):
    appointment_status_history_id = models.AutoField(primary_key=True)
    appointment = models.ForeignKey(AppointmentschedulingAppointment, models.DO_NOTHING)
    status = models.CharField(max_length=255)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'appointmentscheduling_appointment_status_history'


class AppointmentschedulingAppointmentType(models.Model):
    appointment_type_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=1024, blank=True, null=True)
    duration = models.IntegerField()
    uuid = models.CharField(unique=True, max_length=38)
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    retired = models.IntegerField()
    retired_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='retired_by', blank=True, null=True)
    date_retired = models.DateTimeField(blank=True, null=True)
    retire_reason = models.CharField(max_length=255, blank=True, null=True)
    confidential = models.IntegerField()
    visit_type = models.ForeignKey('VisitType', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'appointmentscheduling_appointment_type'


class AppointmentschedulingBlockTypeMap(models.Model):
    appointment_type = models.OneToOneField(AppointmentschedulingAppointmentType, models.DO_NOTHING, primary_key=True)
    appointment_block = models.ForeignKey(AppointmentschedulingAppointmentBlock, models.DO_NOTHING)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'appointmentscheduling_block_type_map'
        unique_together = (('appointment_type', 'appointment_block'),)


class AppointmentschedulingProviderSchedule(models.Model):
    provider_schedule_id = models.AutoField(primary_key=True)
    location = models.ForeignKey('Location', models.DO_NOTHING)
    provider = models.ForeignKey('Provider', models.DO_NOTHING, blank=True, null=True)
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    start_time = models.TimeField()
    end_time = models.TimeField()
    uuid = models.CharField(unique=True, max_length=38)
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    voided = models.IntegerField()
    voided_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='voided_by', blank=True, null=True)
    date_voided = models.DateTimeField(blank=True, null=True)
    void_reason = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'appointmentscheduling_provider_schedule'


class AppointmentschedulingProviderTypeMap(models.Model):
    appointment_type = models.OneToOneField(AppointmentschedulingAppointmentType, models.DO_NOTHING, primary_key=True)
    provider_schedule = models.ForeignKey(AppointmentschedulingProviderSchedule, models.DO_NOTHING)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'appointmentscheduling_provider_type_map'
        unique_together = (('appointment_type', 'provider_schedule'),)


class AppointmentschedulingTimeSlot(models.Model):
    time_slot_id = models.AutoField(primary_key=True)
    appointment_block = models.ForeignKey(AppointmentschedulingAppointmentBlock, models.DO_NOTHING)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    uuid = models.CharField(unique=True, max_length=38)
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    voided = models.IntegerField()
    voided_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='voided_by', blank=True, null=True)
    date_voided = models.DateTimeField(blank=True, null=True)
    void_reason = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'appointmentscheduling_time_slot'


class CalculationRegistration(models.Model):
    calculation_registration_id = models.AutoField(primary_key=True)
    token = models.CharField(unique=True, max_length=255)
    provider_class_name = models.CharField(max_length=512)
    calculation_name = models.CharField(max_length=512)
    configuration = models.TextField(blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'calculation_registration'


class CareSetting(models.Model):
    care_setting_id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)
    care_setting_type = models.CharField(max_length=50)
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    retired = models.IntegerField()
    retired_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='retired_by', blank=True, null=True)
    date_retired = models.DateTimeField(blank=True, null=True)
    retire_reason = models.CharField(max_length=255, blank=True, null=True)
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'care_setting'


class ChartsearchBookmark(models.Model):
    bookmark_id = models.AutoField(primary_key=True)
    bookmark_name = models.TextField()
    search_phrase = models.TextField()
    selected_categories = models.TextField(blank=True, null=True)
    uuid = models.CharField(max_length=38, blank=True, null=True)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    patient = models.ForeignKey('Patient', models.DO_NOTHING)
    default_search = models.IntegerField()

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'chartsearch_bookmark'


class ChartsearchCategories(models.Model):
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    filter_query = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    uuid = models.CharField(max_length=38)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'chartsearch_categories'


class ChartsearchCategoryDisplayname(models.Model):
    displayname_id = models.AutoField(primary_key=True)
    uuid = models.CharField(max_length=38)
    diplay_name = models.CharField(max_length=15)
    preference = models.ForeignKey('ChartsearchPreference', models.DO_NOTHING)
    category = models.ForeignKey(ChartsearchCategories, models.DO_NOTHING)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'chartsearch_category_displayname'


class ChartsearchHistory(models.Model):
    search_id = models.AutoField(primary_key=True)
    search_phrase = models.TextField()
    last_searched_at = models.DateTimeField()
    uuid = models.CharField(max_length=38, blank=True, null=True)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    patient = models.ForeignKey('Patient', models.DO_NOTHING)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'chartsearch_history'


class ChartsearchNote(models.Model):
    note_id = models.AutoField(primary_key=True)
    comment = models.TextField()
    search_phrase = models.TextField()
    priority = models.TextField()
    created_or_last_modified_at = models.DateTimeField()
    uuid = models.CharField(max_length=38, blank=True, null=True)
    display_color = models.CharField(max_length=10, blank=True, null=True)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    patient = models.ForeignKey('Patient', models.DO_NOTHING)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'chartsearch_note'


class ChartsearchPreference(models.Model):
    preference_id = models.AutoField(primary_key=True)
    uuid = models.CharField(max_length=38)
    enable_history = models.IntegerField()
    enable_bookmark = models.IntegerField()
    enable_notes = models.IntegerField()
    enable_duplicateresults = models.IntegerField()
    enable_multiplefiltering = models.IntegerField()
    enable_quicksearches = models.IntegerField()
    enable_defaultsearch = models.IntegerField()
    personalnotes_colors = models.CharField(max_length=255, blank=True, null=True)
    user = models.ForeignKey('Users', models.DO_NOTHING)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'chartsearch_preference'


class ChartsearchSynonymGroups(models.Model):
    group_id = models.IntegerField(primary_key=True)
    group_name = models.CharField(max_length=255)
    is_category = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'chartsearch_synonym_groups'


class ChartsearchSynonyms(models.Model):
    synonym_id = models.AutoField(primary_key=True)
    group = models.ForeignKey(ChartsearchSynonymGroups, models.DO_NOTHING)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'chartsearch_synonyms'


class ClobDatatypeStorage(models.Model):
    uuid = models.CharField(unique=True, max_length=38)
    value = models.TextField()

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'clob_datatype_storage'


class Cohort(models.Model):
    cohort_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=1000, blank=True, null=True)
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    voided = models.IntegerField()
    voided_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='voided_by', blank=True, null=True)
    date_voided = models.DateTimeField(blank=True, null=True)
    void_reason = models.CharField(max_length=255, blank=True, null=True)
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'cohort'


class CohortMember(models.Model):
    cohort = models.ForeignKey(Cohort, models.DO_NOTHING)
    patient = models.ForeignKey('Patient', models.DO_NOTHING)
    cohort_member_id = models.AutoField(primary_key=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    voided = models.IntegerField()
    voided_by = models.IntegerField(blank=True, null=True)
    date_voided = models.DateTimeField(blank=True, null=True)
    void_reason = models.CharField(max_length=255, blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'cohort_member'


# important to understand concepts. Please read at least this:
# https://wiki.openmrs.org/display/docs/Concept+Dictionary+Basics
class Concept(models.Model):
    concept_id = models.AutoField(primary_key=True)
    retired = models.IntegerField()
    short_name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    form_text = models.TextField(blank=True, null=True)
    datatype = models.ForeignKey('ConceptDatatype', models.DO_NOTHING)
    # the type of concept, e.g. Test, Procedure, etc.
    class_field = models.ForeignKey('ConceptClass', models.DO_NOTHING, db_column='class_id')  # Field renamed because it was a Python reserved word.
    is_set = models.IntegerField()
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator', related_name="concepts_created")
    date_created = models.DateTimeField()
    version = models.CharField(max_length=50, blank=True, null=True)
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', blank=True, null=True, related_name="concepts_changed")
    date_changed = models.DateTimeField(blank=True, null=True)
    retired_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='retired_by', blank=True, null=True, related_name="concepts_retired")
    date_retired = models.DateTimeField(blank=True, null=True)
    retire_reason = models.CharField(max_length=255, blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38)

    def __str__(self: 'Concept'):
        # there can be multiple ConceptNames per locale, so we pick the preferred one
        return self.conceptname_set.get(locale='en', locale_preferred=1).name

    class Meta:
        managed = False
        db_table = 'concept'


class ConceptAnswer(models.Model):
    concept_answer_id = models.AutoField(primary_key=True)
    concept = models.ForeignKey(Concept, models.DO_NOTHING)
    answer_concept = models.ForeignKey(Concept, models.DO_NOTHING, db_column='answer_concept', blank=True, null=True)
    answer_drug = models.ForeignKey('Drug', models.DO_NOTHING, db_column='answer_drug', blank=True, null=True)
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    sort_weight = models.FloatField(blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'concept_answer'


class ConceptAttribute(models.Model):
    concept_attribute_id = models.AutoField(primary_key=True)
    concept = models.ForeignKey(Concept, models.DO_NOTHING)
    attribute_type = models.ForeignKey('ConceptAttributeType', models.DO_NOTHING)
    value_reference = models.TextField()
    uuid = models.CharField(unique=True, max_length=38)
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    voided = models.IntegerField()
    voided_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='voided_by', blank=True, null=True)
    date_voided = models.DateTimeField(blank=True, null=True)
    void_reason = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'concept_attribute'


class ConceptAttributeType(models.Model):
    concept_attribute_type_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=1024, blank=True, null=True)
    datatype = models.CharField(max_length=255, blank=True, null=True)
    datatype_config = models.TextField(blank=True, null=True)
    preferred_handler = models.CharField(max_length=255, blank=True, null=True)
    handler_config = models.TextField(blank=True, null=True)
    min_occurs = models.IntegerField()
    max_occurs = models.IntegerField(blank=True, null=True)
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    retired = models.IntegerField()
    retired_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='retired_by', blank=True, null=True)
    date_retired = models.DateTimeField(blank=True, null=True)
    retire_reason = models.CharField(max_length=255, blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'concept_attribute_type'


class ConceptClass(models.Model):
    concept_class_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    retired = models.IntegerField()
    retired_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='retired_by', blank=True, null=True)
    date_retired = models.DateTimeField(blank=True, null=True)
    retire_reason = models.CharField(max_length=255, blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38)
    date_changed = models.DateTimeField(blank=True, null=True)
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', blank=True, null=True)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'concept_class'


class ConceptComplex(models.Model):
    concept = models.OneToOneField(Concept, models.DO_NOTHING, primary_key=True)
    handler = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'concept_complex'


class ConceptDatatype(models.Model):
    concept_datatype_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    hl7_abbreviation = models.CharField(max_length=3, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    retired = models.IntegerField()
    retired_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='retired_by', blank=True, null=True)
    date_retired = models.DateTimeField(blank=True, null=True)
    retire_reason = models.CharField(max_length=255, blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'concept_datatype'


class ConceptDescription(models.Model):
    concept_description_id = models.AutoField(primary_key=True)
    concept = models.ForeignKey(Concept, models.DO_NOTHING)
    description = models.TextField()
    locale = models.CharField(max_length=50)
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'concept_description'


class ConceptMapType(models.Model):
    concept_map_type_id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    is_hidden = models.IntegerField()
    retired = models.IntegerField()
    retired_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='retired_by', blank=True, null=True)
    date_retired = models.DateTimeField(blank=True, null=True)
    retire_reason = models.CharField(max_length=255, blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'concept_map_type'


class ConceptName(models.Model):
    concept_name_id = models.AutoField(primary_key=True)
    concept = models.ForeignKey(Concept, models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=255)
    locale = models.CharField(max_length=50)
    locale_preferred = models.IntegerField(blank=True, null=True)
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator', related_name="conceptnames_created")
    date_created = models.DateTimeField()
    concept_name_type = models.CharField(max_length=50, blank=True, null=True)
    voided = models.IntegerField()
    voided_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='voided_by', blank=True, null=True, related_name="conceptnames_voided")
    date_voided = models.DateTimeField(blank=True, null=True)
    void_reason = models.CharField(max_length=255, blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38)
    date_changed = models.DateTimeField(blank=True, null=True)
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', blank=True, null=True, related_name="conceptnames_changed")

    def __str__(self: 'ConceptName'):
        return self.name

    class Meta:
        managed = False
        db_table = 'concept_name'


# ConceptNameTag is not used so often:
# https://talk.openmrs.org/t/whats-the-purpose-and-use-of-concept-name-tag/3368/3
class ConceptNameTag(models.Model):
    concept_name_tag_id = models.AutoField(primary_key=True)
    tag = models.CharField(unique=True, max_length=50)
    description = models.TextField(blank=True, null=True)
    creator = models.IntegerField()
    date_created = models.DateTimeField()
    voided = models.IntegerField()
    voided_by = models.IntegerField(blank=True, null=True)
    date_voided = models.DateTimeField(blank=True, null=True)
    void_reason = models.CharField(max_length=255, blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38)
    date_changed = models.DateTimeField(blank=True, null=True)
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', blank=True, null=True)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'concept_name_tag'


class ConceptNameTagMap(models.Model):
    concept_name = models.ForeignKey(ConceptName, models.DO_NOTHING)
    concept_name_tag = models.ForeignKey(ConceptNameTag, models.DO_NOTHING)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'concept_name_tag_map'


class ConceptNumeric(models.Model):
    concept = models.OneToOneField(Concept, models.DO_NOTHING, primary_key=True)
    hi_absolute = models.FloatField(blank=True, null=True)
    hi_critical = models.FloatField(blank=True, null=True)
    hi_normal = models.FloatField(blank=True, null=True)
    low_absolute = models.FloatField(blank=True, null=True)
    low_critical = models.FloatField(blank=True, null=True)
    low_normal = models.FloatField(blank=True, null=True)
    units = models.CharField(max_length=50, blank=True, null=True)
    allow_decimal = models.IntegerField(blank=True, null=True)
    display_precision = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'concept_numeric'


class ConceptProposal(models.Model):
    concept_proposal_id = models.AutoField(primary_key=True)
    concept = models.ForeignKey(Concept, models.DO_NOTHING, blank=True, null=True)
    encounter = models.ForeignKey('Encounter', models.DO_NOTHING, blank=True, null=True)
    original_text = models.CharField(max_length=255)
    final_text = models.CharField(max_length=255, blank=True, null=True)
    obs = models.ForeignKey('Obs', models.DO_NOTHING, blank=True, null=True)
    obs_concept = models.ForeignKey(Concept, models.DO_NOTHING, blank=True, null=True)
    state = models.CharField(max_length=32)
    comments = models.CharField(max_length=255, blank=True, null=True)
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    locale = models.CharField(max_length=50)
    uuid = models.CharField(unique=True, max_length=38)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'concept_proposal'


class ConceptProposalTagMap(models.Model):
    concept_proposal = models.ForeignKey(ConceptProposal, models.DO_NOTHING)
    concept_name_tag = models.ForeignKey(ConceptNameTag, models.DO_NOTHING)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'concept_proposal_tag_map'


class ConceptReferenceMap(models.Model):
    concept_map_id = models.AutoField(primary_key=True)
    concept_reference_term = models.ForeignKey('ConceptReferenceTerm', models.DO_NOTHING)
    concept_map_type = models.ForeignKey(ConceptMapType, models.DO_NOTHING)
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    concept = models.ForeignKey(Concept, models.DO_NOTHING)
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'concept_reference_map'


class ConceptReferenceSource(models.Model):
    concept_source_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.TextField()
    hl7_code = models.CharField(unique=True, max_length=50, blank=True, null=True)
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    retired = models.IntegerField()
    retired_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='retired_by', blank=True, null=True)
    date_retired = models.DateTimeField(blank=True, null=True)
    retire_reason = models.CharField(max_length=255, blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38)
    unique_id = models.CharField(unique=True, max_length=250, blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', blank=True, null=True)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'concept_reference_source'


class ConceptReferenceTerm(models.Model):
    concept_reference_term_id = models.AutoField(primary_key=True)
    concept_source = models.ForeignKey(ConceptReferenceSource, models.DO_NOTHING)
    name = models.CharField(max_length=255, blank=True, null=True)
    code = models.CharField(max_length=255)
    version = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    date_changed = models.DateTimeField(blank=True, null=True)
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', blank=True, null=True)
    retired = models.IntegerField()
    retired_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='retired_by', blank=True, null=True)
    date_retired = models.DateTimeField(blank=True, null=True)
    retire_reason = models.CharField(max_length=255, blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'concept_reference_term'


class ConceptReferenceTermMap(models.Model):
    concept_reference_term_map_id = models.AutoField(primary_key=True)
    term_a = models.ForeignKey(ConceptReferenceTerm, models.DO_NOTHING)
    term_b = models.ForeignKey(ConceptReferenceTerm, models.DO_NOTHING)
    a_is_to_b = models.ForeignKey(ConceptMapType, models.DO_NOTHING)
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'concept_reference_term_map'


class ConceptSet(models.Model):
    concept_set_id = models.AutoField(primary_key=True)
    concept_id = models.IntegerField()
    # The field 'concept_set' clashes with the field 'concept_set_id' from model 'openmrs.conceptset'.
    # appending _omrs to disambiguate, and make clear that this follows the OpenMRS API
    concept_set_omrs = models.ForeignKey(Concept, models.DO_NOTHING, db_column='concept_set')
    sort_weight = models.FloatField(blank=True, null=True)
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    uuid = models.CharField(unique=True, max_length=38)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'concept_set'


class ConceptStateConversion(models.Model):
    concept_state_conversion_id = models.AutoField(primary_key=True)
    concept = models.ForeignKey(Concept, models.DO_NOTHING, blank=True, null=True)
    program_workflow = models.ForeignKey('ProgramWorkflow', models.DO_NOTHING, blank=True, null=True)
    program_workflow_state = models.ForeignKey('ProgramWorkflowState', models.DO_NOTHING, blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'concept_state_conversion'
        unique_together = (('program_workflow', 'concept'),)


class ConceptStopWord(models.Model):
    concept_stop_word_id = models.AutoField(primary_key=True)
    word = models.CharField(max_length=50)
    locale = models.CharField(max_length=50, blank=True, null=True)
    uuid = models.CharField(max_length=38)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'concept_stop_word'
        unique_together = (('word', 'locale'),)


class Conditions(models.Model):
    condition_id = models.AutoField(primary_key=True)
    additional_detail = models.CharField(max_length=255, blank=True, null=True)
    previous_version = models.ForeignKey('self', models.DO_NOTHING, db_column='previous_version', blank=True, null=True)
    condition_coded = models.ForeignKey(Concept, models.DO_NOTHING, db_column='condition_coded', blank=True, null=True)
    condition_non_coded = models.CharField(max_length=255, blank=True, null=True)
    condition_coded_name = models.ForeignKey(ConceptName, models.DO_NOTHING, db_column='condition_coded_name', blank=True, null=True)
    clinical_status = models.CharField(max_length=50)
    verification_status = models.CharField(max_length=50, blank=True, null=True)
    onset_date = models.DateTimeField(blank=True, null=True)
    date_created = models.DateTimeField()
    voided = models.IntegerField()
    date_voided = models.DateTimeField(blank=True, null=True)
    void_reason = models.CharField(max_length=255, blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38, blank=True, null=True)
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    voided_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='voided_by', blank=True, null=True)
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', blank=True, null=True)
    patient = models.ForeignKey('Patient', models.DO_NOTHING)
    end_date = models.DateTimeField(blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    encounter = models.ForeignKey('Encounter', models.DO_NOTHING, blank=True, null=True)
    form_namespace_and_path = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'conditions'


class Drug(models.Model):
    drug_id = models.AutoField(primary_key=True)
    concept = models.ForeignKey(Concept, models.DO_NOTHING)
    name = models.CharField(max_length=255, blank=True, null=True)
    combination = models.IntegerField()
    dosage_form = models.ForeignKey(Concept, models.DO_NOTHING, db_column='dosage_form', blank=True, null=True)
    maximum_daily_dose = models.FloatField(blank=True, null=True)
    minimum_daily_dose = models.FloatField(blank=True, null=True)
    route = models.ForeignKey(Concept, models.DO_NOTHING, db_column='route', blank=True, null=True)
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    retired = models.IntegerField()
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    retired_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='retired_by', blank=True, null=True)
    date_retired = models.DateTimeField(blank=True, null=True)
    retire_reason = models.CharField(max_length=255, blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38)
    strength = models.CharField(max_length=255, blank=True, null=True)
    dose_limit_units = models.ForeignKey(Concept, models.DO_NOTHING, db_column='dose_limit_units', blank=True, null=True)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'drug'


class DrugIngredient(models.Model):
    drug = models.OneToOneField(Drug, models.DO_NOTHING, primary_key=True)
    ingredient = models.ForeignKey(Concept, models.DO_NOTHING)
    uuid = models.CharField(unique=True, max_length=38)
    strength = models.FloatField(blank=True, null=True)
    units = models.ForeignKey(Concept, models.DO_NOTHING, db_column='units', blank=True, null=True)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'drug_ingredient'
        unique_together = (('drug', 'ingredient'),)


class DrugOrder(models.Model):
    order = models.OneToOneField('Orders', models.DO_NOTHING, primary_key=True)
    drug_inventory = models.ForeignKey(Drug, models.DO_NOTHING, blank=True, null=True)
    dose = models.FloatField(blank=True, null=True)
    as_needed = models.IntegerField(blank=True, null=True)
    dosing_type = models.CharField(max_length=255, blank=True, null=True)
    quantity = models.FloatField(blank=True, null=True)
    as_needed_condition = models.CharField(max_length=255, blank=True, null=True)
    num_refills = models.IntegerField(blank=True, null=True)
    dosing_instructions = models.TextField(blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    duration_units = models.ForeignKey(Concept, models.DO_NOTHING, db_column='duration_units', blank=True, null=True)
    quantity_units = models.ForeignKey(Concept, models.DO_NOTHING, db_column='quantity_units', blank=True, null=True)
    route = models.ForeignKey(Concept, models.DO_NOTHING, db_column='route', blank=True, null=True)
    dose_units = models.ForeignKey(Concept, models.DO_NOTHING, db_column='dose_units', blank=True, null=True)
    frequency = models.ForeignKey('OrderFrequency', models.DO_NOTHING, db_column='frequency', blank=True, null=True)
    brand_name = models.CharField(max_length=255, blank=True, null=True)
    dispense_as_written = models.IntegerField()
    drug_non_coded = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'drug_order'


class DrugReferenceMap(models.Model):
    drug_reference_map_id = models.AutoField(primary_key=True)
    drug = models.ForeignKey(Drug, models.DO_NOTHING)
    term = models.ForeignKey(ConceptReferenceTerm, models.DO_NOTHING)
    concept_map_type = models.ForeignKey(ConceptMapType, models.DO_NOTHING, db_column='concept_map_type')
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    retired = models.IntegerField()
    retired_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='retired_by', blank=True, null=True)
    date_retired = models.DateTimeField(blank=True, null=True)
    retire_reason = models.CharField(max_length=255, blank=True, null=True)
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'drug_reference_map'


class EmrapiConditions(models.Model):
    condition_id = models.AutoField(primary_key=True)
    previous_condition = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    patient = models.ForeignKey('Patient', models.DO_NOTHING)
    status = models.CharField(max_length=255)
    concept = models.ForeignKey(Concept, models.DO_NOTHING)
    condition_non_coded = models.CharField(max_length=1024, blank=True, null=True)
    onset_date = models.DateTimeField(blank=True, null=True)
    additional_detail = models.CharField(max_length=1024, blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    end_reason = models.ForeignKey(Concept, models.DO_NOTHING, db_column='end_reason', blank=True, null=True)
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    voided = models.IntegerField()
    voided_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='voided_by', blank=True, null=True)
    date_voided = models.DateTimeField(blank=True, null=True)
    void_reason = models.CharField(max_length=255, blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'emrapi_conditions'


class Encounter(models.Model):
    encounter_id = models.AutoField(primary_key=True)
    encounter_type = models.ForeignKey('EncounterType', models.DO_NOTHING, db_column='encounter_type')
    patient = models.ForeignKey('Patient', models.DO_NOTHING)
    location = models.ForeignKey('Location', models.DO_NOTHING, blank=True, null=True)
    form = models.ForeignKey('Form', models.DO_NOTHING, blank=True, null=True)
    encounter_datetime = models.DateTimeField()
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    voided = models.IntegerField()
    voided_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='voided_by', blank=True, null=True)
    date_voided = models.DateTimeField(blank=True, null=True)
    void_reason = models.CharField(max_length=255, blank=True, null=True)
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    visit = models.ForeignKey('Visit', models.DO_NOTHING, blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'encounter'


class EncounterDiagnosis(models.Model):
    diagnosis_id = models.AutoField(primary_key=True)
    diagnosis_coded = models.ForeignKey(Concept, models.DO_NOTHING, db_column='diagnosis_coded', blank=True, null=True)
    diagnosis_non_coded = models.CharField(max_length=255, blank=True, null=True)
    diagnosis_coded_name = models.ForeignKey(ConceptName, models.DO_NOTHING, db_column='diagnosis_coded_name', blank=True, null=True)
    encounter = models.ForeignKey(Encounter, models.DO_NOTHING)
    patient = models.ForeignKey('Patient', models.DO_NOTHING)
    condition = models.ForeignKey(Conditions, models.DO_NOTHING, blank=True, null=True)
    certainty = models.CharField(max_length=255)
    rank = models.IntegerField()
    uuid = models.CharField(unique=True, max_length=38)
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    voided = models.IntegerField()
    voided_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='voided_by', blank=True, null=True)
    date_voided = models.DateTimeField(blank=True, null=True)
    void_reason = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'encounter_diagnosis'


class EncounterProvider(models.Model):
    encounter_provider_id = models.AutoField(primary_key=True)
    encounter = models.ForeignKey(Encounter, models.DO_NOTHING)
    provider = models.ForeignKey('Provider', models.DO_NOTHING)
    encounter_role = models.ForeignKey('EncounterRole', models.DO_NOTHING)
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    voided = models.IntegerField()
    date_voided = models.DateTimeField(blank=True, null=True)
    voided_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='voided_by', blank=True, null=True)
    void_reason = models.CharField(max_length=255, blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'encounter_provider'


class EncounterRole(models.Model):
    encounter_role_id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=255)
    description = models.CharField(max_length=1024, blank=True, null=True)
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    retired = models.IntegerField()
    retired_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='retired_by', blank=True, null=True)
    date_retired = models.DateTimeField(blank=True, null=True)
    retire_reason = models.CharField(max_length=255, blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'encounter_role'


class EncounterType(models.Model):
    encounter_type_id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=50)
    description = models.TextField(blank=True, null=True)
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    retired = models.IntegerField()
    retired_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='retired_by', blank=True, null=True)
    date_retired = models.DateTimeField(blank=True, null=True)
    retire_reason = models.CharField(max_length=255, blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38)
    edit_privilege = models.ForeignKey('Privilege', models.DO_NOTHING, db_column='edit_privilege', blank=True, null=True)
    view_privilege = models.ForeignKey('Privilege', models.DO_NOTHING, db_column='view_privilege', blank=True, null=True)
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'encounter_type'


class FhirConceptSource(models.Model):
    fhir_concept_source_id = models.AutoField(primary_key=True)
    concept_source = models.ForeignKey(ConceptReferenceSource, models.DO_NOTHING, blank=True, null=True)
    url = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    retired = models.IntegerField()
    retired_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='retired_by', blank=True, null=True)
    date_retired = models.DateTimeField(blank=True, null=True)
    retire_reason = models.CharField(max_length=255, blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'fhir_concept_source'


class FhirDiagnosticReport(models.Model):
    diagnostic_report_id = models.AutoField(primary_key=True)
    status = models.CharField(max_length=50)
    concept = models.ForeignKey(Concept, models.DO_NOTHING, blank=True, null=True)
    subject = models.ForeignKey('Patient', models.DO_NOTHING, blank=True, null=True)
    encounter = models.ForeignKey(Encounter, models.DO_NOTHING, blank=True, null=True)
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)
    voided = models.IntegerField()
    voided_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='voided_by', blank=True, null=True)
    date_voided = models.DateTimeField(blank=True, null=True)
    void_reason = models.CharField(max_length=255, blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'fhir_diagnostic_report'


class FhirDiagnosticReportPerformers(models.Model):
    diagnostic_report = models.OneToOneField(FhirDiagnosticReport, models.DO_NOTHING, primary_key=True)
    provider = models.ForeignKey('Provider', models.DO_NOTHING)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'fhir_diagnostic_report_performers'
        unique_together = (('diagnostic_report', 'provider'),)


class FhirDiagnosticReportResults(models.Model):
    diagnostic_report = models.OneToOneField(FhirDiagnosticReport, models.DO_NOTHING, primary_key=True)
    obs = models.ForeignKey('Obs', models.DO_NOTHING)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'fhir_diagnostic_report_results'
        unique_together = (('diagnostic_report', 'obs'),)


class FhirDurationUnitMap(models.Model):
    duration_unit_map_id = models.AutoField(primary_key=True)
    concept = models.ForeignKey(Concept, models.DO_NOTHING, blank=True, null=True)
    unit_of_time = models.CharField(max_length=20)
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    retired = models.IntegerField()
    retired_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='retired_by', blank=True, null=True)
    date_retired = models.DateTimeField(blank=True, null=True)
    retired_reason = models.CharField(max_length=255, blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=36)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'fhir_duration_unit_map'


class FhirEncounterClassMap(models.Model):
    encounter_class_map_id = models.AutoField(primary_key=True)
    location = models.ForeignKey('Location', models.DO_NOTHING, blank=True, null=True)
    encounter_class = models.CharField(max_length=255, blank=True, null=True)
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    retired = models.IntegerField()
    retired_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='retired_by', blank=True, null=True)
    date_retired = models.DateTimeField(blank=True, null=True)
    retired_reason = models.CharField(max_length=255, blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=36)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'fhir_encounter_class_map'


class FhirObservationCategoryMap(models.Model):
    observation_category_map_id = models.AutoField(primary_key=True)
    concept_class = models.ForeignKey(ConceptClass, models.DO_NOTHING, blank=True, null=True)
    observation_category = models.CharField(max_length=255)
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    retired = models.IntegerField()
    retired_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='retired_by', blank=True, null=True)
    date_retired = models.DateTimeField(blank=True, null=True)
    retired_reason = models.CharField(max_length=255, blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=36)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'fhir_observation_category_map'


class FhirPatientIdentifierSystem(models.Model):
    fhir_patient_identifier_system_id = models.AutoField(primary_key=True)
    patient_identifier_type = models.ForeignKey('PatientIdentifierType', models.DO_NOTHING, blank=True, null=True)
    url = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    retired = models.IntegerField()
    retired_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='retired_by', blank=True, null=True)
    date_retired = models.DateTimeField(blank=True, null=True)
    retire_reason = models.CharField(max_length=255, blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'fhir_patient_identifier_system'


class FhirReference(models.Model):
    reference_id = models.AutoField(primary_key=True)
    target_type = models.CharField(max_length=255)
    reference = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)
    retired = models.IntegerField()
    retired_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='retired_by', blank=True, null=True)
    date_retired = models.DateTimeField(blank=True, null=True)
    retire_reason = models.CharField(max_length=255, blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38)
    target_uuid = models.CharField(unique=True, max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'fhir_reference'


class FhirTask(models.Model):
    task_id = models.AutoField(primary_key=True)
    status = models.CharField(max_length=255)
    status_reason = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38)
    intent = models.CharField(max_length=255)
    owner_reference = models.ForeignKey(FhirReference, models.DO_NOTHING, blank=True, null=True)
    encounter_reference = models.ForeignKey(FhirReference, models.DO_NOTHING, blank=True, null=True)
    for_reference = models.ForeignKey(FhirReference, models.DO_NOTHING, blank=True, null=True)
    based_on = models.CharField(max_length=255, blank=True, null=True)
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)
    retired = models.IntegerField()
    retired_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='retired_by', blank=True, null=True)
    date_retired = models.DateTimeField(blank=True, null=True)
    retire_reason = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'fhir_task'


class FhirTaskBasedOnReference(models.Model):
    task = models.ForeignKey(FhirTask, models.DO_NOTHING)
    reference = models.OneToOneField(FhirReference, models.DO_NOTHING)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'fhir_task_based_on_reference'


class FhirTaskInput(models.Model):
    task_input_id = models.AutoField(primary_key=True)
    task = models.ForeignKey(FhirTask, models.DO_NOTHING, blank=True, null=True)
    type = models.ForeignKey(Concept, models.DO_NOTHING, blank=True, null=True)
    value_datetime = models.DateTimeField(blank=True, null=True)
    value_numeric = models.FloatField(blank=True, null=True)
    value_text = models.CharField(max_length=255, blank=True, null=True)
    value_reference = models.ForeignKey(FhirReference, models.DO_NOTHING, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)
    retired = models.IntegerField()
    retired_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='retired_by', blank=True, null=True)
    date_retired = models.DateTimeField(blank=True, null=True)
    retire_reason = models.CharField(max_length=255, blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'fhir_task_input'


class FhirTaskOutput(models.Model):
    task_output_id = models.AutoField(primary_key=True)
    task = models.ForeignKey(FhirTask, models.DO_NOTHING, blank=True, null=True)
    type = models.ForeignKey(Concept, models.DO_NOTHING)
    value_datetime = models.DateTimeField(blank=True, null=True)
    value_numeric = models.FloatField(blank=True, null=True)
    value_text = models.CharField(max_length=255, blank=True, null=True)
    value_reference = models.ForeignKey(FhirReference, models.DO_NOTHING, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)
    retired = models.IntegerField()
    retired_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='retired_by', blank=True, null=True)
    date_retired = models.DateTimeField(blank=True, null=True)
    retire_reason = models.CharField(max_length=255, blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'fhir_task_output'


class Field(models.Model):
    field_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    field_type = models.ForeignKey('FieldType', models.DO_NOTHING, db_column='field_type', blank=True, null=True)
    concept = models.ForeignKey(Concept, models.DO_NOTHING, blank=True, null=True)
    table_name = models.CharField(max_length=50, blank=True, null=True)
    attribute_name = models.CharField(max_length=50, blank=True, null=True)
    default_value = models.TextField(blank=True, null=True)
    select_multiple = models.IntegerField()
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    retired = models.IntegerField()
    retired_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='retired_by', blank=True, null=True)
    date_retired = models.DateTimeField(blank=True, null=True)
    retire_reason = models.CharField(max_length=255, blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'field'


class FieldAnswer(models.Model):
    field = models.OneToOneField(Field, models.DO_NOTHING, primary_key=True)
    answer = models.ForeignKey(Concept, models.DO_NOTHING)
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    uuid = models.CharField(unique=True, max_length=38)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'field_answer'
        unique_together = (('field', 'answer'),)


class FieldType(models.Model):
    field_type_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    is_set = models.IntegerField()
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    uuid = models.CharField(unique=True, max_length=38)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'field_type'


class Form(models.Model):
    form_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    version = models.CharField(max_length=50)
    build = models.IntegerField(blank=True, null=True)
    published = models.IntegerField()
    xslt = models.TextField(blank=True, null=True)
    template = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    encounter_type = models.ForeignKey(EncounterType, models.DO_NOTHING, db_column='encounter_type', blank=True, null=True)
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    retired = models.IntegerField()
    retired_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='retired_by', blank=True, null=True)
    date_retired = models.DateTimeField(blank=True, null=True)
    retired_reason = models.CharField(max_length=255, blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'form'


class FormField(models.Model):
    form_field_id = models.AutoField(primary_key=True)
    form = models.ForeignKey(Form, models.DO_NOTHING)
    field = models.ForeignKey(Field, models.DO_NOTHING)
    field_number = models.IntegerField(blank=True, null=True)
    field_part = models.CharField(max_length=5, blank=True, null=True)
    page_number = models.IntegerField(blank=True, null=True)
    parent_form_field = models.ForeignKey('self', models.DO_NOTHING, db_column='parent_form_field', blank=True, null=True)
    min_occurs = models.IntegerField(blank=True, null=True)
    max_occurs = models.IntegerField(blank=True, null=True)
    required = models.IntegerField()
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    sort_weight = models.FloatField(blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'form_field'


class FormResource(models.Model):
    form_resource_id = models.AutoField(primary_key=True)
    form = models.ForeignKey(Form, models.DO_NOTHING)
    name = models.CharField(max_length=255)
    value_reference = models.TextField()
    datatype = models.CharField(max_length=255, blank=True, null=True)
    datatype_config = models.TextField(blank=True, null=True)
    preferred_handler = models.CharField(max_length=255, blank=True, null=True)
    handler_config = models.TextField(blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38)
    date_changed = models.DateTimeField(blank=True, null=True)
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', blank=True, null=True)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'form_resource'
        unique_together = (('form', 'name'),)


class GlobalProperty(models.Model):
    property = models.CharField(primary_key=True, max_length=255)
    property_value = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38)
    datatype = models.CharField(max_length=255, blank=True, null=True)
    datatype_config = models.TextField(blank=True, null=True)
    preferred_handler = models.CharField(max_length=255, blank=True, null=True)
    handler_config = models.TextField(blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', blank=True, null=True)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'global_property'


class Hl7InArchive(models.Model):
    hl7_in_archive_id = models.AutoField(primary_key=True)
    hl7_source = models.IntegerField()
    hl7_source_key = models.CharField(max_length=255, blank=True, null=True)
    hl7_data = models.TextField()
    date_created = models.DateTimeField()
    message_state = models.IntegerField(blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'hl7_in_archive'


class Hl7InError(models.Model):
    hl7_in_error_id = models.AutoField(primary_key=True)
    hl7_source = models.IntegerField()
    hl7_source_key = models.TextField(blank=True, null=True)
    hl7_data = models.TextField()
    error = models.CharField(max_length=255)
    error_details = models.TextField(blank=True, null=True)
    date_created = models.DateTimeField()
    uuid = models.CharField(unique=True, max_length=38)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'hl7_in_error'


class Hl7InQueue(models.Model):
    hl7_in_queue_id = models.AutoField(primary_key=True)
    hl7_source = models.ForeignKey('Hl7Source', models.DO_NOTHING, db_column='hl7_source')
    hl7_source_key = models.TextField(blank=True, null=True)
    hl7_data = models.TextField()
    message_state = models.IntegerField()
    date_processed = models.DateTimeField(blank=True, null=True)
    error_msg = models.TextField(blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'hl7_in_queue'


class Hl7Source(models.Model):
    hl7_source_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    uuid = models.CharField(unique=True, max_length=38)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'hl7_source'


class HtmlformentryHtmlForm(models.Model):
    form = models.ForeignKey(Form, models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    xml_data = models.TextField()
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    retired = models.IntegerField()
    uuid = models.CharField(unique=True, max_length=38)
    description = models.CharField(max_length=1000, blank=True, null=True)
    retired_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='retired_by', blank=True, null=True)
    date_retired = models.DateTimeField(blank=True, null=True)
    retire_reason = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'htmlformentry_html_form'


class IdgenAutoGenerationOption(models.Model):
    identifier_type = models.ForeignKey('PatientIdentifierType', models.DO_NOTHING, db_column='identifier_type')
    source = models.ForeignKey('IdgenIdentifierSource', models.DO_NOTHING, db_column='source')
    manual_entry_enabled = models.IntegerField()
    automatic_generation_enabled = models.IntegerField()
    location = models.ForeignKey('Location', models.DO_NOTHING, db_column='location', blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=36)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'idgen_auto_generation_option'


class IdgenIdPool(models.Model):
    id = models.OneToOneField('IdgenIdentifierSource', models.DO_NOTHING, db_column='id', primary_key=True)
    source = models.ForeignKey('IdgenIdentifierSource', models.DO_NOTHING, db_column='source', blank=True, null=True)
    batch_size = models.IntegerField(blank=True, null=True)
    min_pool_size = models.IntegerField(blank=True, null=True)
    sequential = models.IntegerField()
    refill_with_scheduled_task = models.IntegerField()

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'idgen_id_pool'


class IdgenIdentifierSource(models.Model):
    uuid = models.CharField(max_length=38)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=1000, blank=True, null=True)
    identifier_type = models.ForeignKey('PatientIdentifierType', models.DO_NOTHING, db_column='identifier_type')
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    retired = models.IntegerField()
    retired_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='retired_by', blank=True, null=True)
    date_retired = models.DateTimeField(blank=True, null=True)
    retire_reason = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'idgen_identifier_source'


class IdgenLogEntry(models.Model):
    source = models.ForeignKey(IdgenIdentifierSource, models.DO_NOTHING, db_column='source')
    identifier = models.CharField(max_length=50)
    date_generated = models.DateTimeField()
    generated_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='generated_by')
    comment = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'idgen_log_entry'


class IdgenPooledIdentifier(models.Model):
    uuid = models.CharField(max_length=38)
    pool = models.ForeignKey(IdgenIdPool, models.DO_NOTHING)
    identifier = models.CharField(max_length=50)
    date_used = models.DateTimeField(blank=True, null=True)
    comment = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'idgen_pooled_identifier'


class IdgenRemoteSource(models.Model):
    id = models.OneToOneField(IdgenIdentifierSource, models.DO_NOTHING, db_column='id', primary_key=True)
    url = models.CharField(max_length=255)
    user = models.CharField(max_length=50, blank=True, null=True)
    password = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'idgen_remote_source'


class IdgenReservedIdentifier(models.Model):
    source = models.ForeignKey(IdgenIdentifierSource, models.DO_NOTHING, db_column='source')
    identifier = models.CharField(max_length=50)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'idgen_reserved_identifier'


class IdgenSeqIdGen(models.Model):
    id = models.OneToOneField(IdgenIdentifierSource, models.DO_NOTHING, db_column='id', primary_key=True)
    next_sequence_value = models.IntegerField()
    base_character_set = models.CharField(max_length=255)
    first_identifier_base = models.CharField(max_length=50)
    prefix = models.CharField(max_length=100, blank=True, null=True)
    suffix = models.CharField(max_length=20, blank=True, null=True)
    min_length = models.IntegerField(blank=True, null=True)
    max_length = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'idgen_seq_id_gen'


class Liquibasechangelog(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=63)  # Field name made lowercase.
    author = models.CharField(db_column='AUTHOR', max_length=63)  # Field name made lowercase.
    filename = models.CharField(db_column='FILENAME', max_length=200)  # Field name made lowercase.
    dateexecuted = models.DateTimeField(db_column='DATEEXECUTED')  # Field name made lowercase.
    orderexecuted = models.IntegerField(db_column='ORDEREXECUTED')  # Field name made lowercase.
    exectype = models.CharField(db_column='EXECTYPE', max_length=10)  # Field name made lowercase.
    md5sum = models.CharField(db_column='MD5SUM', max_length=35, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='DESCRIPTION', max_length=255, blank=True, null=True)  # Field name made lowercase.
    comments = models.CharField(db_column='COMMENTS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    tag = models.CharField(db_column='TAG', max_length=255, blank=True, null=True)  # Field name made lowercase.
    liquibase = models.CharField(db_column='LIQUIBASE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    contexts = models.CharField(db_column='CONTEXTS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    labels = models.CharField(db_column='LABELS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    deployment_id = models.CharField(db_column='DEPLOYMENT_ID', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'liquibasechangelog'
        unique_together = (('id', 'author', 'filename'),)


class Liquibasechangeloglock(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    locked = models.IntegerField(db_column='LOCKED')  # Field name made lowercase.
    lockgranted = models.DateTimeField(db_column='LOCKGRANTED', blank=True, null=True)  # Field name made lowercase.
    lockedby = models.CharField(db_column='LOCKEDBY', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'liquibasechangeloglock'


class Location(models.Model):
    location_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)
    address1 = models.CharField(max_length=255, blank=True, null=True)
    address2 = models.CharField(max_length=255, blank=True, null=True)
    city_village = models.CharField(max_length=255, blank=True, null=True)
    state_province = models.CharField(max_length=255, blank=True, null=True)
    postal_code = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    latitude = models.CharField(max_length=50, blank=True, null=True)
    longitude = models.CharField(max_length=50, blank=True, null=True)
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    county_district = models.CharField(max_length=255, blank=True, null=True)
    address3 = models.CharField(max_length=255, blank=True, null=True)
    address4 = models.CharField(max_length=255, blank=True, null=True)
    address5 = models.CharField(max_length=255, blank=True, null=True)
    address6 = models.CharField(max_length=255, blank=True, null=True)
    retired = models.IntegerField()
    retired_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='retired_by', blank=True, null=True)
    date_retired = models.DateTimeField(blank=True, null=True)
    retire_reason = models.CharField(max_length=255, blank=True, null=True)
    parent_location = models.ForeignKey('self', models.DO_NOTHING, db_column='parent_location', blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38)
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    address7 = models.CharField(max_length=255, blank=True, null=True)
    address8 = models.CharField(max_length=255, blank=True, null=True)
    address9 = models.CharField(max_length=255, blank=True, null=True)
    address10 = models.CharField(max_length=255, blank=True, null=True)
    address11 = models.CharField(max_length=255, blank=True, null=True)
    address12 = models.CharField(max_length=255, blank=True, null=True)
    address13 = models.CharField(max_length=255, blank=True, null=True)
    address14 = models.CharField(max_length=255, blank=True, null=True)
    address15 = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'location'


class LocationAttribute(models.Model):
    location_attribute_id = models.AutoField(primary_key=True)
    location = models.ForeignKey(Location, models.DO_NOTHING)
    attribute_type = models.ForeignKey('LocationAttributeType', models.DO_NOTHING)
    value_reference = models.TextField()
    uuid = models.CharField(unique=True, max_length=38)
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    voided = models.IntegerField()
    voided_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='voided_by', blank=True, null=True)
    date_voided = models.DateTimeField(blank=True, null=True)
    void_reason = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'location_attribute'


class LocationAttributeType(models.Model):
    location_attribute_type_id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=255)
    description = models.CharField(max_length=1024, blank=True, null=True)
    datatype = models.CharField(max_length=255, blank=True, null=True)
    datatype_config = models.TextField(blank=True, null=True)
    preferred_handler = models.CharField(max_length=255, blank=True, null=True)
    handler_config = models.TextField(blank=True, null=True)
    min_occurs = models.IntegerField()
    max_occurs = models.IntegerField(blank=True, null=True)
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    retired = models.IntegerField()
    retired_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='retired_by', blank=True, null=True)
    date_retired = models.DateTimeField(blank=True, null=True)
    retire_reason = models.CharField(max_length=255, blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'location_attribute_type'


class LocationTag(models.Model):
    location_tag_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255, blank=True, null=True)
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    retired = models.IntegerField()
    retired_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='retired_by', blank=True, null=True)
    date_retired = models.DateTimeField(blank=True, null=True)
    retire_reason = models.CharField(max_length=255, blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38)
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'location_tag'


class LocationTagMap(models.Model):
    location = models.OneToOneField(Location, models.DO_NOTHING, primary_key=True)
    location_tag = models.ForeignKey(LocationTag, models.DO_NOTHING)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'location_tag_map'
        unique_together = (('location', 'location_tag'),)


class MetadatamappingMetadataSet(models.Model):
    metadata_set_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=1024, blank=True, null=True)
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    retired = models.IntegerField()
    date_retired = models.DateTimeField(blank=True, null=True)
    retired_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='retired_by', blank=True, null=True)
    retire_reason = models.CharField(max_length=255, blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'metadatamapping_metadata_set'


class MetadatamappingMetadataSetMember(models.Model):
    metadata_set_member_id = models.AutoField(primary_key=True)
    metadata_set = models.ForeignKey(MetadatamappingMetadataSet, models.DO_NOTHING)
    metadata_class = models.CharField(max_length=1024)
    metadata_uuid = models.CharField(max_length=38)
    sort_weight = models.FloatField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=1024, blank=True, null=True)
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    retired = models.IntegerField()
    date_retired = models.DateTimeField(blank=True, null=True)
    retired_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='retired_by', blank=True, null=True)
    retire_reason = models.CharField(max_length=255, blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'metadatamapping_metadata_set_member'
        unique_together = (('metadata_set', 'metadata_uuid'),)


class MetadatamappingMetadataSource(models.Model):
    metadata_source_id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=255)
    description = models.CharField(max_length=1024, blank=True, null=True)
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', blank=True, null=True)
    date_created = models.DateTimeField()
    date_changed = models.DateTimeField(blank=True, null=True)
    retired = models.IntegerField()
    date_retired = models.DateTimeField(blank=True, null=True)
    retired_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='retired_by', blank=True, null=True)
    retire_reason = models.CharField(max_length=255, blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'metadatamapping_metadata_source'


class MetadatamappingMetadataTermMapping(models.Model):
    metadata_term_mapping_id = models.AutoField(primary_key=True)
    metadata_source = models.ForeignKey(MetadatamappingMetadataSource, models.DO_NOTHING)
    code = models.CharField(max_length=255)
    metadata_class = models.CharField(max_length=1024, blank=True, null=True)
    metadata_uuid = models.CharField(max_length=38, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=1024, blank=True, null=True)
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    retired = models.IntegerField()
    date_retired = models.DateTimeField(blank=True, null=True)
    retired_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='retired_by', blank=True, null=True)
    retire_reason = models.CharField(max_length=255, blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'metadatamapping_metadata_term_mapping'
        unique_together = (('metadata_source', 'code'),)


class MetadatasharingExportedPackage(models.Model):
    exported_package_id = models.AutoField(primary_key=True)
    uuid = models.CharField(unique=True, max_length=38)
    group_uuid = models.CharField(max_length=38)
    version = models.IntegerField()
    published = models.IntegerField()
    date_created = models.DateTimeField()
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=256)
    content = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'metadatasharing_exported_package'


class MetadatasharingImportedItem(models.Model):
    imported_item_id = models.AutoField(primary_key=True)
    uuid = models.CharField(max_length=38)
    classname = models.CharField(max_length=256)
    existing_uuid = models.CharField(max_length=38, blank=True, null=True)
    date_imported = models.DateTimeField(blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    import_type = models.IntegerField(blank=True, null=True)
    assessed = models.IntegerField()

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'metadatasharing_imported_item'


class MetadatasharingImportedPackage(models.Model):
    imported_package_id = models.AutoField(primary_key=True)
    uuid = models.CharField(unique=True, max_length=38)
    group_uuid = models.CharField(max_length=38)
    subscription_url = models.CharField(max_length=512, blank=True, null=True)
    subscription_status = models.IntegerField(blank=True, null=True)
    date_created = models.DateTimeField()
    date_imported = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=64, blank=True, null=True)
    description = models.CharField(max_length=256)
    import_config = models.CharField(max_length=1024, blank=True, null=True)
    remote_version = models.IntegerField(blank=True, null=True)
    version = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'metadatasharing_imported_package'


class Note(models.Model):
    note_id = models.IntegerField(primary_key=True)
    note_type = models.CharField(max_length=50, blank=True, null=True)
    patient = models.ForeignKey('Patient', models.DO_NOTHING, blank=True, null=True)
    obs = models.ForeignKey('Obs', models.DO_NOTHING, blank=True, null=True)
    encounter = models.ForeignKey(Encounter, models.DO_NOTHING, blank=True, null=True)
    text = models.TextField()
    priority = models.IntegerField(blank=True, null=True)
    parent = models.ForeignKey('self', models.DO_NOTHING, db_column='parent', blank=True, null=True)
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'note'


class NotificationAlert(models.Model):
    alert_id = models.AutoField(primary_key=True)
    text = models.CharField(max_length=512)
    satisfied_by_any = models.IntegerField()
    alert_read = models.IntegerField()
    date_to_expire = models.DateTimeField(blank=True, null=True)
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'notification_alert'


class NotificationAlertRecipient(models.Model):
    alert = models.OneToOneField(NotificationAlert, models.DO_NOTHING, primary_key=True)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    alert_read = models.IntegerField()
    date_changed = models.DateTimeField(blank=True, null=True)
    uuid = models.CharField(max_length=38)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'notification_alert_recipient'
        unique_together = (('alert', 'user'),)


class NotificationTemplate(models.Model):
    template_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    template = models.TextField(blank=True, null=True)
    subject = models.CharField(max_length=100, blank=True, null=True)
    sender = models.CharField(max_length=255, blank=True, null=True)
    recipients = models.CharField(max_length=512, blank=True, null=True)
    ordinal = models.IntegerField(blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'notification_template'


class Obs(models.Model):
    obs_id = models.AutoField(primary_key=True)
    person = models.ForeignKey('Person', models.DO_NOTHING)
    # this defines what this is a measurement of
    concept = models.ForeignKey(Concept, models.DO_NOTHING)
    encounter = models.ForeignKey(Encounter, models.DO_NOTHING, blank=True, null=True)
    order = models.ForeignKey('Orders', models.DO_NOTHING, blank=True, null=True)
    obs_datetime = models.DateTimeField()
    location = models.ForeignKey(Location, models.DO_NOTHING, blank=True, null=True)
    obs_group = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    accession_number = models.CharField(max_length=255, blank=True, null=True)
    value_group_id = models.IntegerField(blank=True, null=True)
    # come up with better related_name when I better understand this relation
    value_coded = models.ForeignKey(Concept, models.DO_NOTHING, db_column='value_coded', blank=True, null=True, related_name="+")
    value_coded_name = models.ForeignKey(ConceptName, models.DO_NOTHING, blank=True, null=True)
    value_drug = models.ForeignKey(Drug, models.DO_NOTHING, db_column='value_drug', blank=True, null=True)
    value_datetime = models.DateTimeField(blank=True, null=True)
    value_numeric = models.FloatField(blank=True, null=True)
    value_modifier = models.CharField(max_length=2, blank=True, null=True)
    value_text = models.TextField(blank=True, null=True)
    value_complex = models.CharField(max_length=1000, blank=True, null=True)
    comments = models.CharField(max_length=255, blank=True, null=True)
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator', related_name="observations_created")
    date_created = models.DateTimeField()
    voided = models.IntegerField()
    voided_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='voided_by', blank=True, null=True)
    date_voided = models.DateTimeField(blank=True, null=True)
    void_reason = models.CharField(max_length=255, blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38)
    previous_version = models.ForeignKey('self', models.DO_NOTHING, db_column='previous_version', blank=True, null=True, related_name="subsequent_versions")
    form_namespace_and_path = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=16)
    interpretation = models.CharField(max_length=32, blank=True, null=True)

    def __str__(self: 'Obs'):
        #return f"{self.concept.short_name} - {self.concept.description}"
        return f"{str(self.concept)} -- {self.value_numeric}"

    class Meta:
        managed = False
        db_table = 'obs'


class OpenconceptlabImport(models.Model):
    import_id = models.BigAutoField(primary_key=True)
    uuid = models.CharField(max_length=38, blank=True, null=True)
    local_date_started = models.DateTimeField()
    local_date_stopped = models.DateTimeField(blank=True, null=True)
    ocl_date_started = models.DateTimeField(blank=True, null=True)
    error_message = models.CharField(max_length=1024, blank=True, null=True)
    release_version = models.CharField(max_length=512, blank=True, null=True)
    subscription_url = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'openconceptlab_import'


class OpenconceptlabItem(models.Model):
    item_id = models.BigAutoField(primary_key=True)
    import_field = models.ForeignKey(OpenconceptlabImport, models.DO_NOTHING, db_column='import_id')  # Field renamed because it was a Python reserved word.
    type = models.CharField(max_length=512)
    uuid = models.CharField(max_length=38, blank=True, null=True)
    version_url = models.CharField(max_length=1024, blank=True, null=True)
    url = models.CharField(max_length=1024, blank=True, null=True)
    hashed_url = models.CharField(max_length=16, blank=True, null=True)
    state = models.IntegerField()
    error_message = models.CharField(max_length=1024, blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'openconceptlab_item'


class OrderFrequency(models.Model):
    order_frequency_id = models.AutoField(primary_key=True)
    concept = models.OneToOneField(Concept, models.DO_NOTHING)
    frequency_per_day = models.FloatField(blank=True, null=True)
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    retired = models.IntegerField()
    retired_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='retired_by', blank=True, null=True)
    date_retired = models.DateTimeField(blank=True, null=True)
    retire_reason = models.CharField(max_length=255, blank=True, null=True)
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'order_frequency'


class OrderGroup(models.Model):
    order_group_id = models.AutoField(primary_key=True)
    order_set = models.ForeignKey('OrderSet', models.DO_NOTHING, blank=True, null=True)
    patient = models.ForeignKey('Patient', models.DO_NOTHING)
    encounter = models.ForeignKey(Encounter, models.DO_NOTHING)
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    voided = models.IntegerField()
    voided_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='voided_by', blank=True, null=True)
    date_voided = models.DateTimeField(blank=True, null=True)
    void_reason = models.CharField(max_length=255, blank=True, null=True)
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38)
    order_group_reason = models.ForeignKey(Concept, models.DO_NOTHING, db_column='order_group_reason', blank=True, null=True)
    parent_order_group = models.ForeignKey('self', models.DO_NOTHING, db_column='parent_order_group', blank=True, null=True)
    previous_order_group = models.ForeignKey('self', models.DO_NOTHING, db_column='previous_order_group', blank=True, null=True)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'order_group'


class OrderGroupAttribute(models.Model):
    order_group_attribute_id = models.AutoField(primary_key=True)
    order_group = models.ForeignKey(OrderGroup, models.DO_NOTHING)
    attribute_type = models.ForeignKey('OrderGroupAttributeType', models.DO_NOTHING)
    value_reference = models.TextField()
    uuid = models.CharField(unique=True, max_length=38)
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    voided = models.IntegerField()
    voided_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='voided_by', blank=True, null=True)
    date_voided = models.DateTimeField(blank=True, null=True)
    void_reason = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'order_group_attribute'


class OrderGroupAttributeType(models.Model):
    order_group_attribute_type_id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=255)
    description = models.CharField(max_length=1024, blank=True, null=True)
    datatype = models.CharField(max_length=255, blank=True, null=True)
    datatype_config = models.TextField(blank=True, null=True)
    preferred_handler = models.CharField(max_length=255, blank=True, null=True)
    handler_config = models.TextField(blank=True, null=True)
    min_occurs = models.IntegerField()
    max_occurs = models.IntegerField(blank=True, null=True)
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    retired = models.IntegerField()
    retired_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='retired_by', blank=True, null=True)
    date_retired = models.DateTimeField(blank=True, null=True)
    retire_reason = models.CharField(max_length=255, blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'order_group_attribute_type'


class OrderSet(models.Model):
    order_set_id = models.AutoField(primary_key=True)
    operator = models.CharField(max_length=50)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=1000, blank=True, null=True)
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    retired = models.IntegerField()
    retired_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='retired_by', blank=True, null=True)
    date_retired = models.DateTimeField(blank=True, null=True)
    retire_reason = models.CharField(max_length=255, blank=True, null=True)
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38)
    category = models.ForeignKey(Concept, models.DO_NOTHING, db_column='category', blank=True, null=True)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'order_set'


class OrderSetAttribute(models.Model):
    order_set_attribute_id = models.AutoField(primary_key=True)
    order_set = models.ForeignKey(OrderSet, models.DO_NOTHING)
    attribute_type = models.ForeignKey('OrderSetAttributeType', models.DO_NOTHING)
    value_reference = models.TextField()
    uuid = models.CharField(unique=True, max_length=38)
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    voided = models.IntegerField()
    voided_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='voided_by', blank=True, null=True)
    date_voided = models.DateTimeField(blank=True, null=True)
    void_reason = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'order_set_attribute'


class OrderSetAttributeType(models.Model):
    order_set_attribute_type_id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=255)
    description = models.CharField(max_length=1024, blank=True, null=True)
    datatype = models.CharField(max_length=255, blank=True, null=True)
    datatype_config = models.TextField(blank=True, null=True)
    preferred_handler = models.CharField(max_length=255, blank=True, null=True)
    handler_config = models.TextField(blank=True, null=True)
    min_occurs = models.IntegerField()
    max_occurs = models.IntegerField(blank=True, null=True)
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    retired = models.IntegerField()
    retired_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='retired_by', blank=True, null=True)
    date_retired = models.DateTimeField(blank=True, null=True)
    retire_reason = models.CharField(max_length=255, blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'order_set_attribute_type'


class OrderSetMember(models.Model):
    order_set_member_id = models.AutoField(primary_key=True)
    order_type = models.ForeignKey('OrderType', models.DO_NOTHING, db_column='order_type')
    order_template = models.TextField(blank=True, null=True)
    order_template_type = models.CharField(max_length=1024, blank=True, null=True)
    order_set = models.ForeignKey(OrderSet, models.DO_NOTHING)
    sequence_number = models.IntegerField()
    concept = models.ForeignKey(Concept, models.DO_NOTHING)
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    retired = models.IntegerField()
    retired_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='retired_by', blank=True, null=True)
    date_retired = models.DateTimeField(blank=True, null=True)
    retire_reason = models.CharField(max_length=255, blank=True, null=True)
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'order_set_member'


class OrderType(models.Model):
    order_type_id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=255)
    description = models.TextField(blank=True, null=True)
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    retired = models.IntegerField()
    retired_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='retired_by', blank=True, null=True)
    date_retired = models.DateTimeField(blank=True, null=True)
    retire_reason = models.CharField(max_length=255, blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38)
    java_class_name = models.CharField(max_length=255)
    parent = models.ForeignKey('self', models.DO_NOTHING, db_column='parent', blank=True, null=True)
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'order_type'


class OrderTypeClassMap(models.Model):
    order_type = models.OneToOneField(OrderType, models.DO_NOTHING, primary_key=True)
    concept_class = models.OneToOneField(ConceptClass, models.DO_NOTHING)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'order_type_class_map'
        unique_together = (('order_type', 'concept_class'),)


class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    order_type = models.ForeignKey(OrderType, models.DO_NOTHING)
    concept_id = models.IntegerField()
    orderer = models.ForeignKey('Provider', models.DO_NOTHING, db_column='orderer')
    encounter = models.ForeignKey(Encounter, models.DO_NOTHING)
    instructions = models.TextField(blank=True, null=True)
    date_activated = models.DateTimeField(blank=True, null=True)
    auto_expire_date = models.DateTimeField(blank=True, null=True)
    date_stopped = models.DateTimeField(blank=True, null=True)
    order_reason = models.ForeignKey(Concept, models.DO_NOTHING, db_column='order_reason', blank=True, null=True)
    order_reason_non_coded = models.CharField(max_length=255, blank=True, null=True)
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    voided = models.IntegerField()
    voided_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='voided_by', blank=True, null=True)
    date_voided = models.DateTimeField(blank=True, null=True)
    void_reason = models.CharField(max_length=255, blank=True, null=True)
    patient = models.ForeignKey('Patient', models.DO_NOTHING)
    accession_number = models.CharField(max_length=255, blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38)
    urgency = models.CharField(max_length=50)
    order_number = models.CharField(max_length=50)
    previous_order = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    order_action = models.CharField(max_length=50)
    comment_to_fulfiller = models.CharField(max_length=1024, blank=True, null=True)
    care_setting = models.ForeignKey(CareSetting, models.DO_NOTHING, db_column='care_setting')
    scheduled_date = models.DateTimeField(blank=True, null=True)
    order_group = models.ForeignKey(OrderGroup, models.DO_NOTHING, blank=True, null=True)
    sort_weight = models.FloatField(blank=True, null=True)
    fulfiller_comment = models.CharField(max_length=1024, blank=True, null=True)
    fulfiller_status = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'orders'


class Patient(models.Model):
    patient = models.OneToOneField('Person', models.DO_NOTHING, primary_key=True, related_name='patient')
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    voided = models.IntegerField()
    voided_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='voided_by', blank=True, null=True)
    date_voided = models.DateTimeField(blank=True, null=True)
    void_reason = models.CharField(max_length=255, blank=True, null=True)
    allergy_status = models.CharField(max_length=50)

    def __str__(self):
        return str(self.patient)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'patient'


class PatientIdentifier(models.Model):
    patient_identifier_id = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient, models.DO_NOTHING)
    identifier = models.CharField(max_length=50)
    identifier_type = models.ForeignKey('PatientIdentifierType', models.DO_NOTHING, db_column='identifier_type')
    preferred = models.IntegerField()
    location = models.ForeignKey(Location, models.DO_NOTHING, blank=True, null=True)
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    date_changed = models.DateTimeField(blank=True, null=True)
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', blank=True, null=True)
    voided = models.IntegerField()
    voided_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='voided_by', blank=True, null=True)
    date_voided = models.DateTimeField(blank=True, null=True)
    void_reason = models.CharField(max_length=255, blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'patient_identifier'


class PatientIdentifierType(models.Model):
    patient_identifier_type_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    format = models.CharField(max_length=255, blank=True, null=True)
    check_digit = models.IntegerField()
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    required = models.IntegerField()
    format_description = models.CharField(max_length=255, blank=True, null=True)
    validator = models.CharField(max_length=200, blank=True, null=True)
    location_behavior = models.CharField(max_length=50, blank=True, null=True)
    retired = models.IntegerField()
    retired_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='retired_by', blank=True, null=True)
    date_retired = models.DateTimeField(blank=True, null=True)
    retire_reason = models.CharField(max_length=255, blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38)
    uniqueness_behavior = models.CharField(max_length=50, blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', blank=True, null=True)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'patient_identifier_type'


class PatientProgram(models.Model):
    patient_program_id = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient, models.DO_NOTHING)
    program = models.ForeignKey('Program', models.DO_NOTHING)
    date_enrolled = models.DateTimeField(blank=True, null=True)
    date_completed = models.DateTimeField(blank=True, null=True)
    location = models.ForeignKey(Location, models.DO_NOTHING, blank=True, null=True)
    outcome_concept = models.ForeignKey(Concept, models.DO_NOTHING, blank=True, null=True)
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    voided = models.IntegerField()
    voided_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='voided_by', blank=True, null=True)
    date_voided = models.DateTimeField(blank=True, null=True)
    void_reason = models.CharField(max_length=255, blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'patient_program'


class PatientProgramAttribute(models.Model):
    patient_program_attribute_id = models.AutoField(primary_key=True)
    patient_program = models.ForeignKey(PatientProgram, models.DO_NOTHING)
    attribute_type = models.ForeignKey('ProgramAttributeType', models.DO_NOTHING)
    value_reference = models.TextField()
    uuid = models.CharField(unique=True, max_length=38)
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    voided = models.IntegerField()
    voided_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='voided_by', blank=True, null=True)
    date_voided = models.DateTimeField(blank=True, null=True)
    void_reason = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'patient_program_attribute'


class PatientState(models.Model):
    patient_state_id = models.AutoField(primary_key=True)
    patient_program = models.ForeignKey(PatientProgram, models.DO_NOTHING)
    state = models.ForeignKey('ProgramWorkflowState', models.DO_NOTHING, db_column='state')
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    voided = models.IntegerField()
    voided_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='voided_by', blank=True, null=True)
    date_voided = models.DateTimeField(blank=True, null=True)
    void_reason = models.CharField(max_length=255, blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'patient_state'


class Person(models.Model):
    person_id = models.AutoField(primary_key=True)
    gender = models.CharField(max_length=50, blank=True, null=True)
    birthdate = models.DateField(blank=True, null=True)
    birthdate_estimated = models.IntegerField()
    dead = models.IntegerField()
    death_date = models.DateTimeField(blank=True, null=True)
    cause_of_death = models.ForeignKey(Concept, models.DO_NOTHING, db_column='cause_of_death', blank=True, null=True)
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator', blank=True, null=True)
    date_created = models.DateTimeField()
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    voided = models.IntegerField()
    voided_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='voided_by', blank=True, null=True)
    date_voided = models.DateTimeField(blank=True, null=True)
    void_reason = models.CharField(max_length=255, blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38)
    deathdate_estimated = models.IntegerField()
    birthtime = models.TimeField(blank=True, null=True)
    cause_of_death_non_coded = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self: 'Person'):
        try:
            name0 = self.personname_set.get(preferred=1)
        except PersonName.DoesNotExist:
            name0 = "NO NAME"
        return f"{str(name0)} // DoB {self.birthdate}"

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'person'


class PersonAddress(models.Model):
    person_address_id = models.AutoField(primary_key=True)
    person = models.ForeignKey(Person, models.DO_NOTHING, blank=True, null=True)
    preferred = models.IntegerField()
    address1 = models.CharField(max_length=255, blank=True, null=True)
    address2 = models.CharField(max_length=255, blank=True, null=True)
    city_village = models.CharField(max_length=255, blank=True, null=True)
    state_province = models.CharField(max_length=255, blank=True, null=True)
    postal_code = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    latitude = models.CharField(max_length=50, blank=True, null=True)
    longitude = models.CharField(max_length=50, blank=True, null=True)
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    voided = models.IntegerField()
    voided_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='voided_by', blank=True, null=True)
    date_voided = models.DateTimeField(blank=True, null=True)
    void_reason = models.CharField(max_length=255, blank=True, null=True)
    county_district = models.CharField(max_length=255, blank=True, null=True)
    address3 = models.CharField(max_length=255, blank=True, null=True)
    address4 = models.CharField(max_length=255, blank=True, null=True)
    address5 = models.CharField(max_length=255, blank=True, null=True)
    address6 = models.CharField(max_length=255, blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38)
    address7 = models.CharField(max_length=255, blank=True, null=True)
    address8 = models.CharField(max_length=255, blank=True, null=True)
    address9 = models.CharField(max_length=255, blank=True, null=True)
    address10 = models.CharField(max_length=255, blank=True, null=True)
    address11 = models.CharField(max_length=255, blank=True, null=True)
    address12 = models.CharField(max_length=255, blank=True, null=True)
    address13 = models.CharField(max_length=255, blank=True, null=True)
    address14 = models.CharField(max_length=255, blank=True, null=True)
    address15 = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'person_address'


class PersonAttribute(models.Model):
    person_attribute_id = models.AutoField(primary_key=True)
    person = models.ForeignKey(Person, models.DO_NOTHING)
    value = models.CharField(max_length=50)
    person_attribute_type = models.ForeignKey('PersonAttributeType', models.DO_NOTHING)
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    voided = models.IntegerField()
    voided_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='voided_by', blank=True, null=True)
    date_voided = models.DateTimeField(blank=True, null=True)
    void_reason = models.CharField(max_length=255, blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'person_attribute'


class PersonAttributeType(models.Model):
    person_attribute_type_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    format = models.CharField(max_length=50, blank=True, null=True)
    foreign_key = models.IntegerField(blank=True, null=True)
    searchable = models.IntegerField()
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    retired = models.IntegerField()
    retired_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='retired_by', blank=True, null=True)
    date_retired = models.DateTimeField(blank=True, null=True)
    retire_reason = models.CharField(max_length=255, blank=True, null=True)
    edit_privilege = models.ForeignKey('Privilege', models.DO_NOTHING, db_column='edit_privilege', blank=True, null=True)
    sort_weight = models.FloatField(blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'person_attribute_type'


class PersonMergeLog(models.Model):
    person_merge_log_id = models.AutoField(primary_key=True)
    winner_person = models.ForeignKey(Person, models.DO_NOTHING)
    loser_person = models.ForeignKey(Person, models.DO_NOTHING)
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    merged_data = models.TextField()
    uuid = models.CharField(unique=True, max_length=38)
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    voided = models.IntegerField()
    voided_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='voided_by', blank=True, null=True)
    date_voided = models.DateTimeField(blank=True, null=True)
    void_reason = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'person_merge_log'


class PersonName(models.Model):
    person_name_id = models.AutoField(primary_key=True)
    preferred = models.IntegerField()
    person = models.ForeignKey(Person, models.DO_NOTHING)
    prefix = models.CharField(max_length=50, blank=True, null=True)
    given_name = models.CharField(max_length=50, blank=True, null=True)
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    family_name_prefix = models.CharField(max_length=50, blank=True, null=True)
    family_name = models.CharField(max_length=50, blank=True, null=True)
    family_name2 = models.CharField(max_length=50, blank=True, null=True)
    family_name_suffix = models.CharField(max_length=50, blank=True, null=True)
    degree = models.CharField(max_length=50, blank=True, null=True)
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator', related_name="person_names_created")
    date_created = models.DateTimeField()
    voided = models.IntegerField()
    voided_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='voided_by', blank=True, null=True, related_name="person_names_voided")
    date_voided = models.DateTimeField(blank=True, null=True)
    void_reason = models.CharField(max_length=255, blank=True, null=True)
    changed_by = models.IntegerField(blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38)

    class Meta:
        managed = False
        db_table = 'person_name'

    def __str__(self):
        # TODO: logic to use all of the other fields to construct correct display name
        return f"{self.family_name}, {self.given_name}"



class Privilege(models.Model):
    privilege = models.CharField(primary_key=True, max_length=255)
    description = models.TextField(blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'privilege'


class Program(models.Model):
    program_id = models.AutoField(primary_key=True)
    concept = models.ForeignKey(Concept, models.DO_NOTHING)
    outcomes_concept = models.ForeignKey(Concept, models.DO_NOTHING, blank=True, null=True)
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    retired = models.IntegerField()
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'program'


class ProgramAttributeType(models.Model):
    program_attribute_type_id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=255)
    description = models.CharField(max_length=1024, blank=True, null=True)
    datatype = models.CharField(max_length=255, blank=True, null=True)
    datatype_config = models.TextField(blank=True, null=True)
    preferred_handler = models.CharField(max_length=255, blank=True, null=True)
    handler_config = models.TextField(blank=True, null=True)
    min_occurs = models.IntegerField()
    max_occurs = models.IntegerField(blank=True, null=True)
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    retired = models.IntegerField()
    retired_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='retired_by', blank=True, null=True)
    date_retired = models.DateTimeField(blank=True, null=True)
    retire_reason = models.CharField(max_length=255, blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'program_attribute_type'


class ProgramWorkflow(models.Model):
    program_workflow_id = models.AutoField(primary_key=True)
    program = models.ForeignKey(Program, models.DO_NOTHING)
    concept = models.ForeignKey(Concept, models.DO_NOTHING)
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    retired = models.IntegerField()
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'program_workflow'


class ProgramWorkflowState(models.Model):
    program_workflow_state_id = models.AutoField(primary_key=True)
    program_workflow = models.ForeignKey(ProgramWorkflow, models.DO_NOTHING)
    concept = models.ForeignKey(Concept, models.DO_NOTHING)
    initial = models.IntegerField()
    terminal = models.IntegerField()
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    retired = models.IntegerField()
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'program_workflow_state'


class Provider(models.Model):
    provider_id = models.AutoField(primary_key=True)
    person = models.ForeignKey(Person, models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    identifier = models.CharField(max_length=255, blank=True, null=True)
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    retired = models.IntegerField()
    retired_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='retired_by', blank=True, null=True)
    date_retired = models.DateTimeField(blank=True, null=True)
    retire_reason = models.CharField(max_length=255, blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38)
    provider_role = models.ForeignKey('ProvidermanagementProviderRole', models.DO_NOTHING, blank=True, null=True)
    role = models.ForeignKey(Concept, models.DO_NOTHING, blank=True, null=True)
    speciality = models.ForeignKey(Concept, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'provider'


class ProviderAttribute(models.Model):
    provider_attribute_id = models.AutoField(primary_key=True)
    provider = models.ForeignKey(Provider, models.DO_NOTHING)
    attribute_type = models.ForeignKey('ProviderAttributeType', models.DO_NOTHING)
    value_reference = models.TextField()
    uuid = models.CharField(unique=True, max_length=38)
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    voided = models.IntegerField()
    voided_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='voided_by', blank=True, null=True)
    date_voided = models.DateTimeField(blank=True, null=True)
    void_reason = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'provider_attribute'


class ProviderAttributeType(models.Model):
    provider_attribute_type_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=1024, blank=True, null=True)
    datatype = models.CharField(max_length=255, blank=True, null=True)
    datatype_config = models.TextField(blank=True, null=True)
    preferred_handler = models.CharField(max_length=255, blank=True, null=True)
    handler_config = models.TextField(blank=True, null=True)
    min_occurs = models.IntegerField()
    max_occurs = models.IntegerField(blank=True, null=True)
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    retired = models.IntegerField()
    retired_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='retired_by', blank=True, null=True)
    date_retired = models.DateTimeField(blank=True, null=True)
    retire_reason = models.CharField(max_length=255, blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'provider_attribute_type'


class ProvidermanagementProviderRole(models.Model):
    provider_role_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=1000, blank=True, null=True)
    creator = models.IntegerField()
    date_created = models.DateTimeField()
    changed_by = models.IntegerField(blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    retired = models.IntegerField()
    retired_by = models.IntegerField(blank=True, null=True)
    date_retired = models.DateTimeField(blank=True, null=True)
    retire_reason = models.CharField(max_length=255, blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'providermanagement_provider_role'


class ProvidermanagementProviderRoleProviderAttributeType(models.Model):
    provider_role = models.ForeignKey(ProvidermanagementProviderRole, models.DO_NOTHING)
    provider_attribute_type = models.ForeignKey(ProviderAttributeType, models.DO_NOTHING)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'providermanagement_provider_role_provider_attribute_type'


class ProvidermanagementProviderRoleRelationshipType(models.Model):
    provider_role = models.ForeignKey(ProvidermanagementProviderRole, models.DO_NOTHING)
    relationship_type = models.ForeignKey('RelationshipType', models.DO_NOTHING)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'providermanagement_provider_role_relationship_type'


class ProvidermanagementProviderRoleSuperviseeProviderRole(models.Model):
    provider_role = models.ForeignKey(ProvidermanagementProviderRole, models.DO_NOTHING)
    supervisee_provider_role = models.ForeignKey(ProvidermanagementProviderRole, models.DO_NOTHING)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'providermanagement_provider_role_supervisee_provider_role'


class ProvidermanagementProviderSuggestion(models.Model):
    provider_suggestion_id = models.AutoField(primary_key=True)
    criteria = models.CharField(max_length=5000)
    evaluator = models.CharField(max_length=255)
    relationship_type = models.ForeignKey('RelationshipType', models.DO_NOTHING)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=1000, blank=True, null=True)
    creator = models.IntegerField()
    date_created = models.DateTimeField()
    changed_by = models.IntegerField(blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    retired = models.IntegerField()
    retired_by = models.IntegerField(blank=True, null=True)
    date_retired = models.DateTimeField(blank=True, null=True)
    retire_reason = models.CharField(max_length=255, blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'providermanagement_provider_suggestion'


class ProvidermanagementSupervisionSuggestion(models.Model):
    supervision_suggestion_id = models.AutoField(primary_key=True)
    criteria = models.CharField(max_length=5000)
    evaluator = models.CharField(max_length=255)
    provider_role = models.ForeignKey(ProvidermanagementProviderRole, models.DO_NOTHING)
    suggestion_type = models.CharField(max_length=50)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=1000, blank=True, null=True)
    creator = models.IntegerField()
    date_created = models.DateTimeField()
    changed_by = models.IntegerField(blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    retired = models.IntegerField()
    retired_by = models.IntegerField(blank=True, null=True)
    date_retired = models.DateTimeField(blank=True, null=True)
    retire_reason = models.CharField(max_length=255, blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'providermanagement_supervision_suggestion'


class Relationship(models.Model):
    relationship_id = models.AutoField(primary_key=True)
    person_a = models.ForeignKey(Person, models.DO_NOTHING, db_column='person_a')
    # The field 'relationship' clashes with the field 'relationship_id' from model 'openmrs.relationship'
    # we work around by appending _omrs
    relationship_omrs = models.ForeignKey('RelationshipType', models.DO_NOTHING, db_column='relationship')
    person_b = models.ForeignKey(Person, models.DO_NOTHING, db_column='person_b')
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    date_changed = models.DateTimeField(blank=True, null=True)
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', blank=True, null=True)
    voided = models.IntegerField()
    voided_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='voided_by', blank=True, null=True)
    date_voided = models.DateTimeField(blank=True, null=True)
    void_reason = models.CharField(max_length=255, blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'relationship'


class RelationshipType(models.Model):
    relationship_type_id = models.AutoField(primary_key=True)
    a_is_to_b = models.CharField(max_length=50)
    b_is_to_a = models.CharField(max_length=50)
    preferred = models.IntegerField()
    weight = models.IntegerField()
    description = models.CharField(max_length=255, blank=True, null=True)
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    retired = models.IntegerField()
    retired_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='retired_by', blank=True, null=True)
    date_retired = models.DateTimeField(blank=True, null=True)
    retire_reason = models.CharField(max_length=255, blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38)
    date_changed = models.DateTimeField(blank=True, null=True)
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', blank=True, null=True)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'relationship_type'


class ReportObject(models.Model):
    report_object_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=1000, blank=True, null=True)
    report_object_type = models.CharField(max_length=255)
    report_object_sub_type = models.CharField(max_length=255)
    xml_data = models.TextField(blank=True, null=True)
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    voided = models.IntegerField()
    voided_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='voided_by', blank=True, null=True)
    date_voided = models.DateTimeField(blank=True, null=True)
    void_reason = models.CharField(max_length=255, blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'report_object'


class ReportSchemaXml(models.Model):
    report_schema_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    xml_data = models.TextField()
    uuid = models.CharField(unique=True, max_length=38)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'report_schema_xml'


class ReportingReportDesign(models.Model):
    uuid = models.CharField(unique=True, max_length=38)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=1000, blank=True, null=True)
    renderer_type = models.CharField(max_length=255)
    properties = models.TextField(blank=True, null=True)
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    retired = models.IntegerField()
    retired_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='retired_by', blank=True, null=True)
    date_retired = models.DateTimeField(blank=True, null=True)
    retire_reason = models.CharField(max_length=255, blank=True, null=True)
    report_definition_uuid = models.CharField(max_length=38)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'reporting_report_design'


class ReportingReportDesignResource(models.Model):
    uuid = models.CharField(unique=True, max_length=38)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=1000, blank=True, null=True)
    report_design = models.ForeignKey(ReportingReportDesign, models.DO_NOTHING)
    content_type = models.CharField(max_length=50, blank=True, null=True)
    extension = models.CharField(max_length=20, blank=True, null=True)
    contents = models.TextField(blank=True, null=True)
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    retired = models.IntegerField()
    retired_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='retired_by', blank=True, null=True)
    date_retired = models.DateTimeField(blank=True, null=True)
    retire_reason = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'reporting_report_design_resource'


class ReportingReportProcessor(models.Model):
    uuid = models.CharField(unique=True, max_length=38)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=1000, blank=True, null=True)
    processor_type = models.CharField(max_length=255)
    configuration = models.TextField(blank=True, null=True)
    run_on_success = models.IntegerField()
    run_on_error = models.IntegerField()
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    retired = models.IntegerField()
    retired_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='retired_by', blank=True, null=True)
    date_retired = models.DateTimeField(blank=True, null=True)
    retire_reason = models.CharField(max_length=255, blank=True, null=True)
    report_design = models.ForeignKey(ReportingReportDesign, models.DO_NOTHING, blank=True, null=True)
    processor_mode = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'reporting_report_processor'


class ReportingReportRequest(models.Model):
    uuid = models.CharField(unique=True, max_length=38)
    base_cohort_uuid = models.CharField(max_length=38, blank=True, null=True)
    base_cohort_parameters = models.TextField(blank=True, null=True)
    report_definition_uuid = models.CharField(max_length=38)
    report_definition_parameters = models.TextField(blank=True, null=True)
    renderer_type = models.CharField(max_length=255)
    renderer_argument = models.CharField(max_length=255, blank=True, null=True)
    requested_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='requested_by')
    request_datetime = models.DateTimeField()
    priority = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    evaluation_start_datetime = models.DateTimeField(blank=True, null=True)
    evaluation_complete_datetime = models.DateTimeField(blank=True, null=True)
    render_complete_datetime = models.DateTimeField(blank=True, null=True)
    description = models.CharField(max_length=1000, blank=True, null=True)
    schedule = models.CharField(max_length=100, blank=True, null=True)
    process_automatically = models.IntegerField()
    minimum_days_to_preserve = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'reporting_report_request'


class Role(models.Model):
    role = models.CharField(primary_key=True, max_length=50)
    description = models.CharField(max_length=255, blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'role'


class RolePrivilege(models.Model):
    role = models.ForeignKey(Role, models.DO_NOTHING, db_column='role')
    privilege = models.OneToOneField(Privilege, models.DO_NOTHING, db_column='privilege', primary_key=True)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'role_privilege'
        unique_together = (('privilege', 'role'),)


class RoleRole(models.Model):
    parent_role = models.OneToOneField(Role, models.DO_NOTHING, db_column='parent_role', primary_key=True)
    child_role = models.ForeignKey(Role, models.DO_NOTHING, db_column='child_role')

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'role_role'
        unique_together = (('parent_role', 'child_role'),)


class SchedulerTaskConfig(models.Model):
    task_config_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=1024, blank=True, null=True)
    schedulable_class = models.TextField(blank=True, null=True)
    start_time = models.DateTimeField(blank=True, null=True)
    start_time_pattern = models.CharField(max_length=50, blank=True, null=True)
    repeat_interval = models.IntegerField()
    start_on_startup = models.IntegerField()
    started = models.IntegerField()
    created_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='created_by', blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    last_execution_time = models.DateTimeField(blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'scheduler_task_config'


class SchedulerTaskConfigProperty(models.Model):
    task_config_property_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    value = models.TextField(blank=True, null=True)
    task_config = models.ForeignKey(SchedulerTaskConfig, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'scheduler_task_config_property'


class SerializedObject(models.Model):
    serialized_object_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=5000, blank=True, null=True)
    type = models.CharField(max_length=255)
    subtype = models.CharField(max_length=255)
    serialization_class = models.CharField(max_length=255)
    serialized_data = models.TextField()
    date_created = models.DateTimeField()
    creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='creator')
    date_changed = models.DateTimeField(blank=True, null=True)
    changed_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='changed_by', blank=True, null=True)
    retired = models.IntegerField()
    date_retired = models.DateTimeField(blank=True, null=True)
    retired_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='retired_by', blank=True, null=True)
    retire_reason = models.CharField(max_length=1000, blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'serialized_object'


class TestOrder(models.Model):
    order = models.OneToOneField(Orders, models.DO_NOTHING, primary_key=True)
    specimen_source = models.ForeignKey(Concept, models.DO_NOTHING, db_column='specimen_source', blank=True, null=True)
    laterality = models.CharField(max_length=20, blank=True, null=True)
    clinical_history = models.TextField(blank=True, null=True)
    frequency = models.ForeignKey(OrderFrequency, models.DO_NOTHING, db_column='frequency', blank=True, null=True)
    number_of_repeats = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'test_order'


class UiframeworkUserDefinedPageView(models.Model):
    page_view_id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=100)
    template_type = models.CharField(max_length=50)
    template_text = models.TextField()
    uuid = models.CharField(unique=True, max_length=38)
    creator = models.IntegerField()
    date_created = models.DateTimeField()

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'uiframework_user_defined_page_view'


class UserProperty(models.Model):
    user = models.OneToOneField('Users', models.DO_NOTHING, primary_key=True)
    property = models.CharField(max_length=100)
    property_value = models.CharField(max_length=255)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'user_property'
        unique_together = (('user', 'property'),)


class UserRole(models.Model):
    user = models.ForeignKey('Users', models.DO_NOTHING)
    role = models.OneToOneField(Role, models.DO_NOTHING, db_column='role', primary_key=True)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'user_role'
        unique_together = (('role', 'user'),)


class Users(models.Model):
    user_id = models.AutoField(primary_key=True)
    system_id = models.CharField(max_length=50)
    username = models.CharField(max_length=50, blank=True, null=True)
    password = models.CharField(max_length=128, blank=True, null=True)
    salt = models.CharField(max_length=128, blank=True, null=True)
    secret_question = models.CharField(max_length=255, blank=True, null=True)
    secret_answer = models.CharField(max_length=255, blank=True, null=True)
    creator = models.ForeignKey('self', models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    changed_by = models.ForeignKey('self', models.DO_NOTHING, db_column='changed_by', blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    person = models.ForeignKey(Person, models.DO_NOTHING)
    retired = models.IntegerField()
    retired_by = models.ForeignKey('self', models.DO_NOTHING, db_column='retired_by', blank=True, null=True)
    date_retired = models.DateTimeField(blank=True, null=True)
    retire_reason = models.CharField(max_length=255, blank=True, null=True)
    uuid = models.CharField(max_length=38)
    activation_key = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(unique=True, max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'users'


class Visit(models.Model):
    visit_id = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient, models.DO_NOTHING)
    visit_type = models.ForeignKey('VisitType', models.DO_NOTHING)
    date_started = models.DateTimeField()
    date_stopped = models.DateTimeField(blank=True, null=True)
    indication_concept = models.ForeignKey(Concept, models.DO_NOTHING, blank=True, null=True)
    location = models.ForeignKey(Location, models.DO_NOTHING, blank=True, null=True)
    creator = models.ForeignKey(Users, models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    changed_by = models.ForeignKey(Users, models.DO_NOTHING, db_column='changed_by', blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    voided = models.IntegerField()
    voided_by = models.ForeignKey(Users, models.DO_NOTHING, db_column='voided_by', blank=True, null=True)
    date_voided = models.DateTimeField(blank=True, null=True)
    void_reason = models.CharField(max_length=255, blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'visit'


class VisitAttribute(models.Model):
    visit_attribute_id = models.AutoField(primary_key=True)
    visit = models.ForeignKey(Visit, models.DO_NOTHING)
    attribute_type = models.ForeignKey('VisitAttributeType', models.DO_NOTHING)
    value_reference = models.TextField()
    uuid = models.CharField(unique=True, max_length=38)
    creator = models.ForeignKey(Users, models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    changed_by = models.ForeignKey(Users, models.DO_NOTHING, db_column='changed_by', blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    voided = models.IntegerField()
    voided_by = models.ForeignKey(Users, models.DO_NOTHING, db_column='voided_by', blank=True, null=True)
    date_voided = models.DateTimeField(blank=True, null=True)
    void_reason = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'visit_attribute'


class VisitAttributeType(models.Model):
    visit_attribute_type_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=1024, blank=True, null=True)
    datatype = models.CharField(max_length=255, blank=True, null=True)
    datatype_config = models.TextField(blank=True, null=True)
    preferred_handler = models.CharField(max_length=255, blank=True, null=True)
    handler_config = models.TextField(blank=True, null=True)
    min_occurs = models.IntegerField()
    max_occurs = models.IntegerField(blank=True, null=True)
    creator = models.ForeignKey(Users, models.DO_NOTHING, db_column='creator')
    date_created = models.DateTimeField()
    changed_by = models.ForeignKey(Users, models.DO_NOTHING, db_column='changed_by', blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    retired = models.IntegerField()
    retired_by = models.ForeignKey(Users, models.DO_NOTHING, db_column='retired_by', blank=True, null=True)
    date_retired = models.DateTimeField(blank=True, null=True)
    retire_reason = models.CharField(max_length=255, blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38)

    class Meta:
        managed = False
        default_related_name = '+'
        db_table = 'visit_attribute_type'


class VisitType(models.Model):
    visit_type_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=1024, blank=True, null=True)
    creator = models.ForeignKey(Users, models.DO_NOTHING, db_column='creator', related_name='VisitTypesCreated')
    date_created = models.DateTimeField()
    changed_by = models.ForeignKey(Users, models.DO_NOTHING, db_column='changed_by', blank=True, null=True, related_name='VisitTypesChanged')
    date_changed = models.DateTimeField(blank=True, null=True)
    retired = models.IntegerField()
    retired_by = models.ForeignKey(Users, models.DO_NOTHING, db_column='retired_by', blank=True, null=True, related_name='VisitTypesRetired')
    date_retired = models.DateTimeField(blank=True, null=True)
    retire_reason = models.CharField(max_length=255, blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=38)

    class Meta:
        managed = False
        db_table = 'visit_type'
