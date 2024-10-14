from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_live_timelines_locale import GetLiveTimelinesLocale
from ...models.get_live_timelines_response_200 import GetLiveTimelinesResponse200
from ...types import Response


def _get_kwargs(
    locale: GetLiveTimelinesLocale,
    format: str = "json",  # Added format parameter with default "json"
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/{locale}/schedules/live/timelines" + f".{format}",  # Append format to URL
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[GetLiveTimelinesResponse200]:
    if response.status_code == HTTPStatus.OK:
        response_200 = GetLiveTimelinesResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[GetLiveTimelinesResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    locale: GetLiveTimelinesLocale,
    *,
    client: AuthenticatedClient,
    format: str = "json",  # Added format parameter with default "json"
) -> Response[GetLiveTimelinesResponse200]:
    """get a list of timelines for live sport events

     Get a list of timelines for sport events which are live right now. Sport events appear in the feed
    10 minutes before the scheduled start time and are removed 10 minutes after the sport event is
    ended.

    Args:
        locale (GetLiveTimelinesLocale):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetLiveTimelinesResponse200]
    """

    kwargs = _get_kwargs(locale=locale, format=format)

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    locale: GetLiveTimelinesLocale,
    *,
    client: AuthenticatedClient,
    format: str = "json",  # Added format parameter to shorthand function as well
) -> Optional[GetLiveTimelinesResponse200]:
    """get a list of timelines for live sport events

     Get a list of timelines for sport events which are live right now. Sport events appear in the feed
    10 minutes before the scheduled start time and are removed 10 minutes after the sport event is
    ended.

    Args:
        locale (GetLiveTimelinesLocale):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetLiveTimelinesResponse200
    """

    return sync_detailed(
        locale=locale,
        client=client,
        format=format,  # Pass format to sync_detailed
    ).parsed


async def asyncio_detailed(
    locale: GetLiveTimelinesLocale,
    *,
    client: AuthenticatedClient,
    format: str = "json",  # Added format parameter with default "json"
) -> Response[GetLiveTimelinesResponse200]:
    """get a list of timelines for live sport events

     Get a list of timelines for sport events which are live right now. Sport events appear in the feed
    10 minutes before the scheduled start time and are removed 10 minutes after the sport event is
    ended.

    Args:
        locale (GetLiveTimelinesLocale):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetLiveTimelinesResponse200]
    """

    kwargs = _get_kwargs(locale=locale, format=format)

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    locale: GetLiveTimelinesLocale,
    *,
    client: AuthenticatedClient,
    format: str = "json",  # Added format parameter to async shorthand function
) -> Optional[GetLiveTimelinesResponse200]:
    """get a list of timelines for live sport events

     Get a list of timelines for sport events which are live right now. Sport events appear in the feed
    10 minutes before the scheduled start time and are removed 10 minutes after the sport event is
    ended.

    Args:
        locale (GetLiveTimelinesLocale):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetLiveTimelinesResponse200
    """

    return (
        await asyncio_detailed(
            locale=locale,
            client=client,
            format=format,  # Pass format to asyncio_detailed
        )
    ).parsed
