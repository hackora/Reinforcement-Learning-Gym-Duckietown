from setuptools import setup

setup(name='duckietown_rl',
      version='1.0',
      install_requires=['gym>=0.5',
                        'gym_duckietown',
                        'gym_duckietown_agent>=2018.08',
                        'sklearn',
                        'torch',
                        'numpy',
                        'matplotlib',
                        'scipy']
      )
