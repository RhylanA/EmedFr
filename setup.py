from setuptools import setup, find_packages

setup(
    name='my-discord-self-embed',
    version='0.1',
    packages=find_packages(),
    license='MIT',
    description='A custom implementation of discord.py-self_embed for selfbots.',
    author='Your Name',
    author_email='your.email@example.com',
    url='https://discord.gg/GYRw6MQGb8',
    download_url='https://discord.gg/GYRw6MQGb8',
    keywords=['discord', 'embed', 'selfbot'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown'
)
