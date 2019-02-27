#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : papi
Version  : 5.7.0
Release  : 1
URL      : http://icl.utk.edu/projects/papi/downloads/papi-5.7.0.tar.gz
Source0  : http://icl.utk.edu/projects/papi/downloads/papi-5.7.0.tar.gz
Summary  : Performance Application Programming Interface
Group    : Development/Tools
License  : LGPL-2.1 MIT
Requires: papi-bin = %{version}-%{release}
Requires: papi-data = %{version}-%{release}
Requires: papi-lib = %{version}-%{release}
Requires: papi-license = %{version}-%{release}
Requires: papi-man = %{version}-%{release}
BuildRequires : buildreq-configure
BuildRequires : buildreq-distutils3
BuildRequires : gfortran

%description
PAPI provides a programmer interface to monitor the performance of
running programs.

%package bin
Summary: bin components for the papi package.
Group: Binaries
Requires: papi-data = %{version}-%{release}
Requires: papi-license = %{version}-%{release}

%description bin
bin components for the papi package.


%package data
Summary: data components for the papi package.
Group: Data

%description data
data components for the papi package.


%package dev
Summary: dev components for the papi package.
Group: Development
Requires: papi-lib = %{version}-%{release}
Requires: papi-bin = %{version}-%{release}
Requires: papi-data = %{version}-%{release}
Provides: papi-devel = %{version}-%{release}

%description dev
dev components for the papi package.


%package lib
Summary: lib components for the papi package.
Group: Libraries
Requires: papi-data = %{version}-%{release}
Requires: papi-license = %{version}-%{release}

%description lib
lib components for the papi package.


%package license
Summary: license components for the papi package.
Group: Default

%description license
license components for the papi package.


%package man
Summary: man components for the papi package.
Group: Default

%description man
man components for the papi package.


%prep
%setup -q -n papi-5.7.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1551311341
export LDFLAGS="${LDFLAGS} -fno-lto"
pushd src
%configure --disable-static
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1551311341
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/papi
cp src/libpfm-3.y/COPYRIGHT %{buildroot}/usr/share/package-licenses/papi/src_libpfm-3.y_COPYRIGHT
cp src/libpfm4/debian/copyright %{buildroot}/usr/share/package-licenses/papi/src_libpfm4_debian_copyright
cp src/perfctr-2.6.x/COPYING %{buildroot}/usr/share/package-licenses/papi/src_perfctr-2.6.x_COPYING
cp src/perfctr-2.7.x/COPYING %{buildroot}/usr/share/package-licenses/papi/src_perfctr-2.7.x_COPYING
pushd src
%make_install
popd

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/papi_avail
/usr/bin/papi_clockres
/usr/bin/papi_command_line
/usr/bin/papi_component_avail
/usr/bin/papi_cost
/usr/bin/papi_decode
/usr/bin/papi_error_codes
/usr/bin/papi_event_chooser
/usr/bin/papi_mem_info
/usr/bin/papi_multiplex_cost
/usr/bin/papi_native_avail
/usr/bin/papi_version
/usr/bin/papi_xml_event_info

%files data
%defattr(-,root,root,-)
/usr/share/papi/papi_events.csv

%files dev
%defattr(-,root,root,-)
/usr/include/*.h
/usr/include/perfmon/perf_event.h
/usr/include/perfmon/pfmlib.h
/usr/include/perfmon/pfmlib_perf_event.h
/usr/lib64/libpapi.so
/usr/lib64/libpfm.so
/usr/lib64/pkgconfig/papi-5.7.0.0.pc
/usr/lib64/pkgconfig/papi-5.7.0.pc
/usr/lib64/pkgconfig/papi-5.pc
/usr/lib64/pkgconfig/papi.pc
/usr/share/man/man3/PAPIF_accum.3
/usr/share/man/man3/PAPIF_accum_counters.3
/usr/share/man/man3/PAPIF_add_event.3
/usr/share/man/man3/PAPIF_add_events.3
/usr/share/man/man3/PAPIF_add_named_event.3
/usr/share/man/man3/PAPIF_assign_eventset_component.3
/usr/share/man/man3/PAPIF_cleanup_eventset.3
/usr/share/man/man3/PAPIF_create_eventset.3
/usr/share/man/man3/PAPIF_destroy_eventset.3
/usr/share/man/man3/PAPIF_enum_event.3
/usr/share/man/man3/PAPIF_epc.3
/usr/share/man/man3/PAPIF_event_code_to_name.3
/usr/share/man/man3/PAPIF_event_name_to_code.3
/usr/share/man/man3/PAPIF_flips.3
/usr/share/man/man3/PAPIF_flops.3
/usr/share/man/man3/PAPIF_get_clockrate.3
/usr/share/man/man3/PAPIF_get_dmem_info.3
/usr/share/man/man3/PAPIF_get_domain.3
/usr/share/man/man3/PAPIF_get_event_info.3
/usr/share/man/man3/PAPIF_get_exe_info.3
/usr/share/man/man3/PAPIF_get_granularity.3
/usr/share/man/man3/PAPIF_get_hardware_info.3
/usr/share/man/man3/PAPIF_get_multiplex.3
/usr/share/man/man3/PAPIF_get_preload.3
/usr/share/man/man3/PAPIF_get_real_cyc.3
/usr/share/man/man3/PAPIF_get_real_nsec.3
/usr/share/man/man3/PAPIF_get_real_usec.3
/usr/share/man/man3/PAPIF_get_virt_cyc.3
/usr/share/man/man3/PAPIF_get_virt_usec.3
/usr/share/man/man3/PAPIF_ipc.3
/usr/share/man/man3/PAPIF_is_initialized.3
/usr/share/man/man3/PAPIF_library_init.3
/usr/share/man/man3/PAPIF_lock.3
/usr/share/man/man3/PAPIF_multiplex_init.3
/usr/share/man/man3/PAPIF_num_cmp_hwctrs.3
/usr/share/man/man3/PAPIF_num_counters.3
/usr/share/man/man3/PAPIF_num_events.3
/usr/share/man/man3/PAPIF_num_hwctrs.3
/usr/share/man/man3/PAPIF_perror.3
/usr/share/man/man3/PAPIF_query_event.3
/usr/share/man/man3/PAPIF_query_named_event.3
/usr/share/man/man3/PAPIF_read.3
/usr/share/man/man3/PAPIF_read_ts.3
/usr/share/man/man3/PAPIF_register_thread.3
/usr/share/man/man3/PAPIF_remove_event.3
/usr/share/man/man3/PAPIF_remove_events.3
/usr/share/man/man3/PAPIF_remove_named_event.3
/usr/share/man/man3/PAPIF_reset.3
/usr/share/man/man3/PAPIF_set_cmp_domain.3
/usr/share/man/man3/PAPIF_set_cmp_granularity.3
/usr/share/man/man3/PAPIF_set_debug.3
/usr/share/man/man3/PAPIF_set_domain.3
/usr/share/man/man3/PAPIF_set_event_domain.3
/usr/share/man/man3/PAPIF_set_granularity.3
/usr/share/man/man3/PAPIF_set_inherit.3
/usr/share/man/man3/PAPIF_set_multiplex.3
/usr/share/man/man3/PAPIF_shutdown.3
/usr/share/man/man3/PAPIF_start.3
/usr/share/man/man3/PAPIF_start_counters.3
/usr/share/man/man3/PAPIF_state.3
/usr/share/man/man3/PAPIF_stop.3
/usr/share/man/man3/PAPIF_stop_counters.3
/usr/share/man/man3/PAPIF_thread_id.3
/usr/share/man/man3/PAPIF_thread_init.3
/usr/share/man/man3/PAPIF_unlock.3
/usr/share/man/man3/PAPIF_unregister_thread.3
/usr/share/man/man3/PAPIF_write.3
/usr/share/man/man3/PAPI_accum.3
/usr/share/man/man3/PAPI_accum_counters.3
/usr/share/man/man3/PAPI_add_event.3
/usr/share/man/man3/PAPI_add_events.3
/usr/share/man/man3/PAPI_add_named_event.3
/usr/share/man/man3/PAPI_addr_range_option_t.3
/usr/share/man/man3/PAPI_address_map_t.3
/usr/share/man/man3/PAPI_all_thr_spec_t.3
/usr/share/man/man3/PAPI_assign_eventset_component.3
/usr/share/man/man3/PAPI_attach.3
/usr/share/man/man3/PAPI_attach_option_t.3
/usr/share/man/man3/PAPI_cleanup_eventset.3
/usr/share/man/man3/PAPI_component_info_t.3
/usr/share/man/man3/PAPI_cpu_option_t.3
/usr/share/man/man3/PAPI_create_eventset.3
/usr/share/man/man3/PAPI_debug_option_t.3
/usr/share/man/man3/PAPI_destroy_eventset.3
/usr/share/man/man3/PAPI_detach.3
/usr/share/man/man3/PAPI_disable_component.3
/usr/share/man/man3/PAPI_disable_component_by_name.3
/usr/share/man/man3/PAPI_dmem_info_t.3
/usr/share/man/man3/PAPI_domain_option_t.3
/usr/share/man/man3/PAPI_enum_cmp_event.3
/usr/share/man/man3/PAPI_enum_event.3
/usr/share/man/man3/PAPI_epc.3
/usr/share/man/man3/PAPI_event_code_to_name.3
/usr/share/man/man3/PAPI_event_info_t.3
/usr/share/man/man3/PAPI_event_name_to_code.3
/usr/share/man/man3/PAPI_exe_info_t.3
/usr/share/man/man3/PAPI_flips.3
/usr/share/man/man3/PAPI_flops.3
/usr/share/man/man3/PAPI_get_cmp_opt.3
/usr/share/man/man3/PAPI_get_component_index.3
/usr/share/man/man3/PAPI_get_component_info.3
/usr/share/man/man3/PAPI_get_dmem_info.3
/usr/share/man/man3/PAPI_get_event_component.3
/usr/share/man/man3/PAPI_get_event_info.3
/usr/share/man/man3/PAPI_get_eventset_component.3
/usr/share/man/man3/PAPI_get_executable_info.3
/usr/share/man/man3/PAPI_get_hardware_info.3
/usr/share/man/man3/PAPI_get_multiplex.3
/usr/share/man/man3/PAPI_get_opt.3
/usr/share/man/man3/PAPI_get_overflow_event_index.3
/usr/share/man/man3/PAPI_get_real_cyc.3
/usr/share/man/man3/PAPI_get_real_nsec.3
/usr/share/man/man3/PAPI_get_real_usec.3
/usr/share/man/man3/PAPI_get_shared_lib_info.3
/usr/share/man/man3/PAPI_get_thr_specific.3
/usr/share/man/man3/PAPI_get_virt_cyc.3
/usr/share/man/man3/PAPI_get_virt_nsec.3
/usr/share/man/man3/PAPI_get_virt_usec.3
/usr/share/man/man3/PAPI_granularity_option_t.3
/usr/share/man/man3/PAPI_hw_info_t.3
/usr/share/man/man3/PAPI_inherit_option_t.3
/usr/share/man/man3/PAPI_ipc.3
/usr/share/man/man3/PAPI_is_initialized.3
/usr/share/man/man3/PAPI_itimer_option_t.3
/usr/share/man/man3/PAPI_library_init.3
/usr/share/man/man3/PAPI_list_events.3
/usr/share/man/man3/PAPI_list_threads.3
/usr/share/man/man3/PAPI_lock.3
/usr/share/man/man3/PAPI_mh_cache_info_t.3
/usr/share/man/man3/PAPI_mh_info_t.3
/usr/share/man/man3/PAPI_mh_level_t.3
/usr/share/man/man3/PAPI_mh_tlb_info_t.3
/usr/share/man/man3/PAPI_mpx_info_t.3
/usr/share/man/man3/PAPI_multiplex_init.3
/usr/share/man/man3/PAPI_multiplex_option_t.3
/usr/share/man/man3/PAPI_num_cmp_hwctrs.3
/usr/share/man/man3/PAPI_num_components.3
/usr/share/man/man3/PAPI_num_counters.3
/usr/share/man/man3/PAPI_num_events.3
/usr/share/man/man3/PAPI_num_hwctrs.3
/usr/share/man/man3/PAPI_option_t.3
/usr/share/man/man3/PAPI_overflow.3
/usr/share/man/man3/PAPI_perror.3
/usr/share/man/man3/PAPI_preload_info_t.3
/usr/share/man/man3/PAPI_profil.3
/usr/share/man/man3/PAPI_query_event.3
/usr/share/man/man3/PAPI_query_named_event.3
/usr/share/man/man3/PAPI_read.3
/usr/share/man/man3/PAPI_read_counters.3
/usr/share/man/man3/PAPI_read_ts.3
/usr/share/man/man3/PAPI_register_thread.3
/usr/share/man/man3/PAPI_remove_event.3
/usr/share/man/man3/PAPI_remove_events.3
/usr/share/man/man3/PAPI_remove_named_event.3
/usr/share/man/man3/PAPI_reset.3
/usr/share/man/man3/PAPI_set_cmp_domain.3
/usr/share/man/man3/PAPI_set_cmp_granularity.3
/usr/share/man/man3/PAPI_set_debug.3
/usr/share/man/man3/PAPI_set_domain.3
/usr/share/man/man3/PAPI_set_granularity.3
/usr/share/man/man3/PAPI_set_multiplex.3
/usr/share/man/man3/PAPI_set_opt.3
/usr/share/man/man3/PAPI_set_thr_specific.3
/usr/share/man/man3/PAPI_shlib_info_t.3
/usr/share/man/man3/PAPI_shutdown.3
/usr/share/man/man3/PAPI_sprofil.3
/usr/share/man/man3/PAPI_sprofil_t.3
/usr/share/man/man3/PAPI_start.3
/usr/share/man/man3/PAPI_start_counters.3
/usr/share/man/man3/PAPI_state.3
/usr/share/man/man3/PAPI_stop.3
/usr/share/man/man3/PAPI_stop_counters.3
/usr/share/man/man3/PAPI_strerror.3
/usr/share/man/man3/PAPI_thread_id.3
/usr/share/man/man3/PAPI_thread_init.3
/usr/share/man/man3/PAPI_unlock.3
/usr/share/man/man3/PAPI_unregister_thread.3
/usr/share/man/man3/PAPI_write.3
/usr/share/man/man3/libpfm.3
/usr/share/man/man3/libpfm_amd64.3
/usr/share/man/man3/libpfm_amd64_fam10h.3
/usr/share/man/man3/libpfm_amd64_fam15h.3
/usr/share/man/man3/libpfm_amd64_fam16h.3
/usr/share/man/man3/libpfm_amd64_fam17h.3
/usr/share/man/man3/libpfm_amd64_k7.3
/usr/share/man/man3/libpfm_amd64_k8.3
/usr/share/man/man3/libpfm_intel_atom.3
/usr/share/man/man3/libpfm_intel_bdw.3
/usr/share/man/man3/libpfm_intel_bdx_unc_cbo.3
/usr/share/man/man3/libpfm_intel_bdx_unc_ha.3
/usr/share/man/man3/libpfm_intel_bdx_unc_imc.3
/usr/share/man/man3/libpfm_intel_bdx_unc_irp.3
/usr/share/man/man3/libpfm_intel_bdx_unc_pcu.3
/usr/share/man/man3/libpfm_intel_bdx_unc_qpi.3
/usr/share/man/man3/libpfm_intel_bdx_unc_r2pcie.3
/usr/share/man/man3/libpfm_intel_bdx_unc_r3qpi.3
/usr/share/man/man3/libpfm_intel_bdx_unc_sbo.3
/usr/share/man/man3/libpfm_intel_bdx_unc_ubo.3
/usr/share/man/man3/libpfm_intel_core.3
/usr/share/man/man3/libpfm_intel_glm.3
/usr/share/man/man3/libpfm_intel_hsw.3
/usr/share/man/man3/libpfm_intel_hswep_unc_cbo.3
/usr/share/man/man3/libpfm_intel_hswep_unc_ha.3
/usr/share/man/man3/libpfm_intel_hswep_unc_imc.3
/usr/share/man/man3/libpfm_intel_hswep_unc_irp.3
/usr/share/man/man3/libpfm_intel_hswep_unc_pcu.3
/usr/share/man/man3/libpfm_intel_hswep_unc_qpi.3
/usr/share/man/man3/libpfm_intel_hswep_unc_r2pcie.3
/usr/share/man/man3/libpfm_intel_hswep_unc_r3qpi.3
/usr/share/man/man3/libpfm_intel_hswep_unc_sbo.3
/usr/share/man/man3/libpfm_intel_hswep_unc_ubo.3
/usr/share/man/man3/libpfm_intel_ivb.3
/usr/share/man/man3/libpfm_intel_ivb_unc.3
/usr/share/man/man3/libpfm_intel_ivbep_unc_cbo.3
/usr/share/man/man3/libpfm_intel_ivbep_unc_ha.3
/usr/share/man/man3/libpfm_intel_ivbep_unc_imc.3
/usr/share/man/man3/libpfm_intel_ivbep_unc_irp.3
/usr/share/man/man3/libpfm_intel_ivbep_unc_pcu.3
/usr/share/man/man3/libpfm_intel_ivbep_unc_qpi.3
/usr/share/man/man3/libpfm_intel_ivbep_unc_r2pcie.3
/usr/share/man/man3/libpfm_intel_ivbep_unc_r3qpi.3
/usr/share/man/man3/libpfm_intel_ivbep_unc_ubo.3
/usr/share/man/man3/libpfm_intel_knc.3
/usr/share/man/man3/libpfm_intel_knl.3
/usr/share/man/man3/libpfm_intel_knm.3
/usr/share/man/man3/libpfm_intel_nhm.3
/usr/share/man/man3/libpfm_intel_nhm_unc.3
/usr/share/man/man3/libpfm_intel_rapl.3
/usr/share/man/man3/libpfm_intel_skl.3
/usr/share/man/man3/libpfm_intel_skx_unc_cha.3
/usr/share/man/man3/libpfm_intel_skx_unc_imc.3
/usr/share/man/man3/libpfm_intel_skx_unc_irp.3
/usr/share/man/man3/libpfm_intel_skx_unc_m2m.3
/usr/share/man/man3/libpfm_intel_skx_unc_m3upi.3
/usr/share/man/man3/libpfm_intel_skx_unc_pcu.3
/usr/share/man/man3/libpfm_intel_skx_unc_ubo.3
/usr/share/man/man3/libpfm_intel_skx_unc_upi.3
/usr/share/man/man3/libpfm_intel_slm.3
/usr/share/man/man3/libpfm_intel_snb.3
/usr/share/man/man3/libpfm_intel_snb_unc.3
/usr/share/man/man3/libpfm_intel_snbep_unc_cbo.3
/usr/share/man/man3/libpfm_intel_snbep_unc_ha.3
/usr/share/man/man3/libpfm_intel_snbep_unc_imc.3
/usr/share/man/man3/libpfm_intel_snbep_unc_pcu.3
/usr/share/man/man3/libpfm_intel_snbep_unc_qpi.3
/usr/share/man/man3/libpfm_intel_snbep_unc_r2pcie.3
/usr/share/man/man3/libpfm_intel_snbep_unc_r3qpi.3
/usr/share/man/man3/libpfm_intel_snbep_unc_ubo.3
/usr/share/man/man3/libpfm_intel_wsm.3
/usr/share/man/man3/libpfm_intel_wsm_unc.3
/usr/share/man/man3/libpfm_intel_x86_arch.3
/usr/share/man/man3/libpfm_perf_event_raw.3
/usr/share/man/man3/pfm_find_event.3
/usr/share/man/man3/pfm_get_event_attr_info.3
/usr/share/man/man3/pfm_get_event_encoding.3
/usr/share/man/man3/pfm_get_event_info.3
/usr/share/man/man3/pfm_get_event_next.3
/usr/share/man/man3/pfm_get_os_event_encoding.3
/usr/share/man/man3/pfm_get_perf_event_encoding.3
/usr/share/man/man3/pfm_get_pmu_info.3
/usr/share/man/man3/pfm_get_version.3
/usr/share/man/man3/pfm_initialize.3
/usr/share/man/man3/pfm_strerror.3
/usr/share/man/man3/pfm_terminate.3

%files lib
%defattr(-,root,root,-)
/usr/lib64/libpapi.so.5
/usr/lib64/libpapi.so.5.7.0
/usr/lib64/libpapi.so.5.7.0.0
/usr/lib64/libpfm.so.4
/usr/lib64/libpfm.so.4.10.1

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/papi/src_libpfm-3.y_COPYRIGHT
/usr/share/package-licenses/papi/src_libpfm4_debian_copyright
/usr/share/package-licenses/papi/src_perfctr-2.6.x_COPYING
/usr/share/package-licenses/papi/src_perfctr-2.7.x_COPYING

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/PAPI_derived_event_files.1
/usr/share/man/man1/papi_avail.1
/usr/share/man/man1/papi_clockres.1
/usr/share/man/man1/papi_command_line.1
/usr/share/man/man1/papi_component_avail.1
/usr/share/man/man1/papi_cost.1
/usr/share/man/man1/papi_decode.1
/usr/share/man/man1/papi_error_codes.1
/usr/share/man/man1/papi_event_chooser.1
/usr/share/man/man1/papi_hybrid_native_avail.1
/usr/share/man/man1/papi_mem_info.1
/usr/share/man/man1/papi_multiplex_cost.1
/usr/share/man/man1/papi_native_avail.1
/usr/share/man/man1/papi_version.1
/usr/share/man/man1/papi_xml_event_info.1
