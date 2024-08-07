from setuptools import setup

package_name = 'turtle_joystick'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='your_name',
    maintainer_email='your_email@example.com',
    description='Joystick control for TurtleSim',
    license='Apache License 2.0',
    entry_points={
        'console_scripts': [
            'joystick_control = turtle_joystick.joystick_control:main',
        ],
    },
)
