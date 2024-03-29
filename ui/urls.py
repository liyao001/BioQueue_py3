from django.conf.urls import url
from . import views

app_name = "ui"

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add-job/$', views.add_job, name='add_job'),
    url(r'^add-step/$', views.add_step, name='add_step'),
    url(r'^batch-job/$', views.batch_job, name='batch_job'),
    url(r'^batch-operation/$', views.batch_operation, name='batch_operation'),
    url(r'^clean-dead-lock/$', views.clean_dead_lock, name='clean_dead_lock'),
    url(r'^create-protocol/$', views.create_protocol, name='create_protocol'),
    url(r'^create-reference-shortcut/$', views.create_reference_shortcut, name='create_reference_shortcut'),
    url(r'^delete-job/$', views.delete_job, name='delete_job'),
    url(r'^delete-job-file/(?P<f>[a-z,A-Z,0-9,/,+,=]*)/$', views.delete_job_file, name='delete_job_file'),
    url(r'^delete-protocol/$', views.delete_protocol, name='delete_protocol'),
    url(r'^delete-reference', views.delete_reference, name='delete_reference'),
    url(r'^delete-upload-file/(?P<f>[a-z,A-Z,0-9,/,+,=]*)/$', views.delete_upload_file, name='delete_upload_file'),
    url(r'^delete-sample/(?P<f>[a-z,A-Z,0-9,/,+,=]*)/$', views.delete_sample, name='delete_sample'),
    url(r'^delete-step/$', views.delete_step, name='delete_step'),
    url(r'^delete-ve/$', views.delete_ve, name='delete_ve'),
    url(r'^download-file/(?P<f>[a-z,A-Z,0-9,/,+,=]*)/$', views.download_file, name='download_file'),
    url(r'^export-protocol', views.export_protocol, name='export_protocol'),
    url(r'^file-support', views.file_support, name='file_support'),
    url(r'^fetch-data', views.fetch_data, name='fetch_data'),
    url(r'^fetch-learning', views.fetch_learning, name='fetch_learning'),
    url(r'^get-learning-result/$', views.get_learning_result, name='get_learning_result'),
    url(r'^get-job-list/$', views.get_job_list, name='get_job_list'),
    url(r'^get-job-file-list/$', views.get_job_file_list, name='get_job_file_list'),
    url(r'^import-learning/$', views.import_learning, name='import_learning'),
    url(r'^import-protocol-by-fetch/$', views.import_protocol_by_fetch, name='import_protocol_by_fetch'),
    url(r'^import-protocol/$', views.import_protocol, name='import_protocol'),
    url(r'^install-ref', views.install_reference, name='install_reference'),
    url(r'^install-tool', views.install_tool, name='install_tool'),
    url(r'^manage-reference', views.manage_reference, name='manage_reference'),
    url(r'^mark-audit', views.mark_wrong_job, name='mark_wrong_job'),
    url(r'^user-reference', views.print_user_reference, name='print_user_reference'),
    url(r'^query-job/$', views.query_job, name='query_job'),
    url(r'^query-job-parameter/$', views.query_job_parameter, name='query_job_parameter'),
    url(r'^query-protocol', views.query_protocol, name='query_protocol'),
    url(r'^query-running-jobs', views.query_running_jobs, name='query_running_jobs'),
    url(r'^query-usage', views.query_usage, name='query_usage'),
    url(r'^register-sample/', views.register_sample, name='register_sample'),
    url(r'^rerun-job/$', views.rerun_job, name='rerun_job'),
    url(r'^resume-job/$', views.resume_job, name='resume_job'),
    url(r'^send-file-as-reference/(?P<f>[a-z,A-Z,0-9,/,+,=]*)/$', views.send_file_as_reference, name='send_file_as_reference'),
    url(r'^settings/$', views.settings, name='settings'),
    url(r'^share-with-peer/$', views.share_with_peer, name='share_with_peer'),
    url(r'^show-job-log/$', views.show_job_log, name='show_job_log'),
    url(r'^show-job-folder/$', views.show_job_folder, name='show_job_folder'),
    url(r'^show-learning/$', views.show_learning, name='show_learning'),
    url(r'^show-learning-steps', views.show_learning_steps, name='show_learning_steps'),
    url(r'^show-step/$', views.show_step, name='show_step'),
    url(r'^show-upload/$', views.show_upload_files, name='show_upload'),
    url(r'^show-workspace/$', views.show_workspace, name='show_workspace'),
    url(r'^terminate-job/$', views.terminate_job, name='terminate_job'),
    url(r'^update-bioqueue/$', views.update_bioqueue, name='update_bioqueue'),
    url(r'^update-comment/$', views.update_comment, name='update_comment'),
    url(r'^update-parameter/$', views.update_parameter, name='update_parameter'),
    url(r'^update-reference/$', views.update_reference, name='update_reference'),
    url(r'^update-step-order/$', views.update_step_order, name='update_step_order'),
    url(r'^update-ve/$', views.update_ve, name='update_ve'),
    url(r'^upload-protocol/$', views.upload_protocol, name='upload_protocol'),
    url(r'^virtual-env/$', views.virtual_environment, name='virtual_env'),
]
