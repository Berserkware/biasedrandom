from distutils.core import setup

setup(
  name = 'biasedrandom',
  packages = ['biasedrandom'],
  version = '0.2',
  license='MIT',
  description = 'A python library for doing biased random based on random module',
  long_description=README,
  long_description_content_type="text/markdown",
  author = 'Caleb M',
  author_email = 'bersekware@gmail.com',
  url = 'https://github.com/Berserkware/biasedrandom',
  download_url = 'https://github.com/Berserkware/biasedrandom/archive/refs/tags/v_02.tar.gz',
  keywords = ['biased', 'random', 'python', 'biasedrandom'],
  install_requires=[],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
