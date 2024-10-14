from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_live_timelines_delta_locale import GetLiveTimelinesDeltaLocale
from ...types import Response


def _get_kwargs(
    locale: GetLiveTimelinesDeltaLocale,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/{locale}/schedules/live/timelines_delta",
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
    if response.status_code == HTTPStatus.OK:
        return None
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    locale: GetLiveTimelinesDeltaLocale,
    *,
    client: AuthenticatedClient,
) -> Response[Any]:
    """get the summary and timelines for all sport events where something happened the last 10 seconds,
    with only the events of the last 10 seconds

     Get the summary and timelines for all sport events where something happened the last 10 seconds,
    with only the events of the last 10 seconds

    Args:
        locale (GetLiveTimelinesDeltaLocale):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        locale=locale,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    locale: GetLiveTimelinesDeltaLocale,
    *,
    client: AuthenticatedClient,
) -> Response[Any]:
    """get the summary and timelines for all sport events where something happened the last 10 seconds,
    with only the events of the last 10 seconds

     Get the summary and timelines for all sport events where something happened the last 10 seconds,
    with only the events of the last 10 seconds

    Args:
        locale (GetLiveTimelinesDeltaLocale):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        locale=locale,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
