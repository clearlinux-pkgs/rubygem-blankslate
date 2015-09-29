#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-blankslate
Version  : 3.1.3
Release  : 5
URL      : https://rubygems.org/downloads/blankslate-3.1.3.gem
Source0  : https://rubygems.org/downloads/blankslate-3.1.3.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
BuildRequires : ruby
BuildRequires : rubygem-diff-lcs
BuildRequires : rubygem-rdoc
BuildRequires : rubygem-rspec
BuildRequires : rubygem-rspec-core
BuildRequires : rubygem-rspec-expectations
BuildRequires : rubygem-rspec-mocks
BuildRequires : rubygem-rspec-support

%description
BlankSlate
===
BlankSlate provides an abstract base class with no predefined
methods (except for <tt>\_\_send__</tt> and <tt>\_\_id__</tt>).
BlankSlate is useful as a base class when writing classes that
depend upon <tt>method_missing</tt> (e.g. dynamic proxies).

%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n blankslate-3.1.3
gem spec %{SOURCE0} -l --ruby > rubygem-blankslate.gemspec

%build
gem build rubygem-blankslate.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
blankslate-3.1.3.gem

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
%{buildroot}%{gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
pushd %{buildroot}%{gem_dir}/gems/blankslate-3.1.3
rspec -I.:lib spec/
popd


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.2.0/cache/blankslate-3.1.3.gem
/usr/lib64/ruby/gems/2.2.0/doc/blankslate-3.1.3/ri/BlankSlate/cdesc-BlankSlate.ri
/usr/lib64/ruby/gems/2.2.0/doc/blankslate-3.1.3/ri/BlankSlate/find_hidden_method-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/blankslate-3.1.3/ri/BlankSlate/hide-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/blankslate-3.1.3/ri/BlankSlate/reveal-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/blankslate-3.1.3/ri/Kernel/blank_slate_method_added-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/blankslate-3.1.3/ri/Kernel/cdesc-Kernel.ri
/usr/lib64/ruby/gems/2.2.0/doc/blankslate-3.1.3/ri/Kernel/method_added-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/blankslate-3.1.3/ri/Module/append_features-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/blankslate-3.1.3/ri/Module/blankslate_original_append_features-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/blankslate-3.1.3/ri/Module/cdesc-Module.ri
/usr/lib64/ruby/gems/2.2.0/doc/blankslate-3.1.3/ri/Object/blank_slate_method_added-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/blankslate-3.1.3/ri/Object/cdesc-Object.ri
/usr/lib64/ruby/gems/2.2.0/doc/blankslate-3.1.3/ri/Object/find_hidden_method-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/blankslate-3.1.3/ri/Object/method_added-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/blankslate-3.1.3/ri/String/_blankslate_as_name-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/blankslate-3.1.3/ri/String/cdesc-String.ri
/usr/lib64/ruby/gems/2.2.0/doc/blankslate-3.1.3/ri/Symbol/_blankslate_as_name-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/blankslate-3.1.3/ri/Symbol/cdesc-Symbol.ri
/usr/lib64/ruby/gems/2.2.0/doc/blankslate-3.1.3/ri/cache.ri
/usr/lib64/ruby/gems/2.2.0/gems/blankslate-3.1.3/Gemfile
/usr/lib64/ruby/gems/2.2.0/gems/blankslate-3.1.3/Gemfile.lock
/usr/lib64/ruby/gems/2.2.0/gems/blankslate-3.1.3/MIT-LICENSE
/usr/lib64/ruby/gems/2.2.0/gems/blankslate-3.1.3/README
/usr/lib64/ruby/gems/2.2.0/gems/blankslate-3.1.3/Rakefile
/usr/lib64/ruby/gems/2.2.0/gems/blankslate-3.1.3/VERSION
/usr/lib64/ruby/gems/2.2.0/gems/blankslate-3.1.3/blankslate.gemspec
/usr/lib64/ruby/gems/2.2.0/gems/blankslate-3.1.3/lib/blankslate.rb
/usr/lib64/ruby/gems/2.2.0/gems/blankslate-3.1.3/spec/blankslate_spec.rb
/usr/lib64/ruby/gems/2.2.0/specifications/blankslate-3.1.3.gemspec
