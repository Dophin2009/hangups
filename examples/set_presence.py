"""Example of using hangups to set presence."""

import asyncio

import hangups

from common import run_example


async def set_presence(client, args):
    request = hangups.hangouts_pb2.SetPresenceRequest(
        request_header=client.get_request_header(),
        status_message_setting=(
            hangups.hangouts_pb2.StatusMessageSetting(
                status_message=[
                    hangups.hangouts_pb2.ChatMessageSpec(
                        segment=[
                            hangups.hangouts_pb2.Segment(
                                type=hangups.hangouts_pb2.SEGMENT_TYPE_TEXT,
                                text='set up hangups',
                                formatting=hangups.hangouts_pb2.Formatting(
                                    bold=False,
                                    italic=False,
                                    strikethrough=False,
                                    underline=False,
                                ),
                            ),
                        ]
                    ),
                ]
            )
        )
    )
    await client.set_presence(request)


if __name__ == '__main__':
    run_example(set_presence)
