from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_live_timelines_delta_locale import GetLiveTimelinesDeltaLocale
from ...models.get_live_timelines_delta_response_200 import GetLiveTimelinesDeltaResponse200
from ...types import Response


def _get_kwargs(
    locale: GetLiveTimelinesDeltaLocale,
    format: str = "json",  # Added format parameter with default "json"
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/{locale}/schedules/live/timelines_delta" + f".{format}",  # Append format to URL
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[GetLiveTimelinesDeltaResponse200]:
    if response.status_code == HTTPStatus.OK:
        response_200 = GetLiveTimelinesDeltaResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[GetLiveTimelinesDeltaResponse200]:
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
    format: str = "json",  # Added format parameter with default "json"
) -> Response[GetLiveTimelinesDeltaResponse200]:
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
        Response[GetLiveTimelinesDeltaResponse200]
    """

    kwargs = _get_kwargs(locale=locale, format=format)

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    locale: GetLiveTimelinesDeltaLocale,
    *,
    client: AuthenticatedClient,
    format: str = "json",  # Added format parameter to shorthand function as well
) -> Optional[GetLiveTimelinesDeltaResponse200]:
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
        GetLiveTimelinesDeltaResponse200
    """

    return sync_detailed(
        locale=locale,
        client=client,
        format=format,  # Pass format to sync_detailed
    ).parsed


async def asyncio_detailed(
    locale: GetLiveTimelinesDeltaLocale,
    *,
    client: AuthenticatedClient,
    format: str = "json",  # Added format parameter with default "json"
) -> Response[GetLiveTimelinesDeltaResponse200]:
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
        Response[GetLiveTimelinesDeltaResponse200]
    """

    kwargs = _get_kwargs(locale=locale, format=format)

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    locale: GetLiveTimelinesDeltaLocale,
    *,
    client: AuthenticatedClient,
    format: str = "json",  # Added format parameter to async shorthand function
) -> Optional[GetLiveTimelinesDeltaResponse200]:
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
        GetLiveTimelinesDeltaResponse200
    """

    return (
        await asyncio_detailed(
            locale=locale,
            client=client,
            format=format,  # Pass format to asyncio_detailed
        )
    ).parsed
