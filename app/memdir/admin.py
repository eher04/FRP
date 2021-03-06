from django.contrib import admin

from memdir import forms
from memdir import models


class InlineHours(admin.TabularInline):
    model = models.HoursOfOperation
    extra = 1


class InlineContact(admin.TabularInline):
    model = models.LocationContact
    extra = 1


class InlineLocation(admin.StackedInline):
    model = models.Location
    inlines = [InlineHours, InlineContact,]
    readonly_fields = ['slug']
    extra = 0
    fieldsets = (
        (None, {
            'fields': (
                'order',
                'frp_program_name',
                'region',
                'community',
                'street',
                'city',
                'province',
                'postal_code',
                'phone',
                'fax',
                'website',
            )
        }),
        ('Mailing Address (if different from physical address)', {
            #'classes': ('collapse',),
            'fields': (
                'mailing_street',
                'mailing_city',
                'mailing_postal_code',
                'mailing_province',
            )
        }),
        ('Programs Offered', {
            'fields': (
                'pcmg_offered',
                'npp_offered',
                'triplep_offered',
            )
        }),

    )



class MemberAdmin(admin.ModelAdmin):
    form = forms.MemberAdminForm
    actions_on_top = True
    actions_on_bottom = True
    list_display = ('agency', 'is_frp_member', 'renewal_date', 'memnum')
    search_fields = ('agency',)
    list_filter = ('is_frp_member', 'renewal_date',)
    date_hierarchy = 'renewal_date'
    ordering = ('agency',)
    change_form_template = 'admin_edit_agency2.html'
    inlines = [InlineLocation,]
    save_on_top = True
    fieldsets = (
        (None, {
            'fields': (
                'agency',
                'street',
                'city',
                'postal_code',
                'province',
                'phone',
                'fax',
                'website',
                'join_date',
                'updated',
                'notes',
            )
        }),
        (#'Contact', {
         None, {
            'fields': (
                'agdirect',
                'agdirect_title',
                'dirphone',
                'email',
            )
        }),
        (#'Membership', {
         None, {
            'fields': (
                'memnum',
                'renewal_date',
                'membership_type',
			)
		}),
		(#'Standards', {
		 None, {
			'fields': (
				'standards_complete',
                'standards_beginning_year',
				'standards_renewal_year',
				'accredited',
            )
        }),
        ('Mailing Address (if different from physical address)', {
            'classes': ('collapse',),
            'fields': (
                'mailing_street',
                'mailing_city',
                'mailing_postal_code',
                'mailing_province',
            )
        }),
        ('Payment Information', {
            'classes': ('collapse',),
            'fields': (
                'fee',
                'receipt',
                'paidfrp',
            )
        }),
        ('Description', {
            'classes': ('collapse',),
            'fields': (
                'description',
            )
        }),
    )


class LocationAdmin(admin.ModelAdmin):
    readonly_fields = ['slug']

admin.site.register(models.Member, MemberAdmin)
admin.site.register(models.Location, LocationAdmin)
admin.site.register(models.HoursOfOperation)
admin.site.register(models.LocationContact)
