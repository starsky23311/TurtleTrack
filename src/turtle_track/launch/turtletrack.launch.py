import os
import launch
from launch_ros.actions import Node
from launch_ros.actions import ComposableNodeContainer
from launch_ros.descriptions import ComposableNode
from ament_index_python.packages import get_package_share_directory
from launch.actions import SetEnvironmentVariable, ExecuteProcess
from launch.substitutions import EnvironmentVariable
from launch.substitutions import LaunchConfiguration
from launch.actions import DeclareLaunchArgument

def generate_launch_description():
    # target_frame = LaunchConfiguration('turtlename', default='turtle1')


    return launch.LaunchDescription([
        DeclareLaunchArgument(
            'target_frame', default_value='turtle1',
            description='Target frame name.'
        ),

        Node(
            package='turtlesim',
            executable='turtlesim_node',
            name='turtle_node'
        ),

        # ExecuteProcess(
        #     cmd=['ros2', 'service', 'call', '/spawn', 'turtlesim/srv/Spawn', '{x: 2, y: 2, theta: 0.2, name: '"turtle2"'}'],
        #     output="screen"
        # ),

        Node(
            package='turtle_track',
            executable='TurtleBroadNode',
            name='broadcaster1',
            parameters=[
                {'turtlename': 'turtle1'}
            ]
        ),


        Node(
            package='turtle_track',
            executable='TurtleBroadNode',
            name='broadcaster2',
            parameters=[
                {'turtlename': 'turtle2'}
            ]
        ),
        Node(
            package='turtle_track',
            executable='TurtleTrackNode',
            name='listener',
            parameters=[
                {'target_frame': LaunchConfiguration('turtlename', default='turtle1')}
            ]
        ),

    ])

