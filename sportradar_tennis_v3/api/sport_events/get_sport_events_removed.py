from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_sport_events_removed_locale import GetSportEventsRemovedLocale
from ...models.get_sport_events_removed_response_200 import GetSportEventsRemovedResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    locale: GetSportEventsRemovedLocale,
    *,
    offset: Union[Unset, int] = 0,
    start: Union[Unset, int] = 0,
    limit: Union[Unset, int] = 200,
    format: str = "json",  # Added format parameter with default "json"
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["offset"] = offset

    params["start"] = start

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/{locale}/sport_events/removed" + f".{format}",  # Append format to URL
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[GetSportEventsRemovedResponse200]:
    if response.status_code == HTTPStatus.OK:
        response_200 = GetSportEventsRemovedResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[GetSportEventsRemovedResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    locale: GetSportEventsRemovedLocale,
    *,
    client: AuthenticatedClient,
    offset: Union[Unset, int] = 0,
    start: Union[Unset, int] = 0,
    limit: Union[Unset, int] = 200,
    format: str = "json",  # Added format parameter with default "json"
) -> Response[GetSportEventsRemovedResponse200]:
    """sport events which has been removed

     Lists sport events which has been removed or disabled.

    Args:
        locale (GetSportEventsRemovedLocale):
        offset (Union[Unset, int]):  Default: 0.
        start (Union[Unset, int]):  Default: 0.
        limit (Union[Unset, int]):  Default: 200.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSportEventsRemovedResponse200]
    """

    kwargs = _get_kwargs(locale=locale, offset=offset, start=start, limit=limit, format=format)

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    locale: GetSportEventsRemovedLocale,
    *,
    client: AuthenticatedClient,
    offset: Union[Unset, int] = 0,
    start: Union[Unset, int] = 0,
    limit: Union[Unset, int] = 200,
    format: str = "json",  # Added format parameter to shorthand function as well
) -> Optional[GetSportEventsRemovedResponse200]:
    """sport events which has been removed

     Lists sport events which has been removed or disabled.

    Args:
        locale (GetSportEventsRemovedLocale):
        offset (Union[Unset, int]):  Default: 0.
        start (Union[Unset, int]):  Default: 0.
        limit (Union[Unset, int]):  Default: 200.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSportEventsRemovedResponse200
    """

    return sync_detailed(
        locale=locale,
        client=client,
        offset=offset,
        start=start,
        limit=limit,
        format=format,  # Pass format to sync_detailed
    ).parsed


async def asyncio_detailed(
    locale: GetSportEventsRemovedLocale,
    *,
    client: AuthenticatedClient,
    offset: Union[Unset, int] = 0,
    start: Union[Unset, int] = 0,
    limit: Union[Unset, int] = 200,
    format: str = "json",  # Added format parameter with default "json"
) -> Response[GetSportEventsRemovedResponse200]:
    """sport events which has been removed

     Lists sport events which has been removed or disabled.

    Args:
        locale (GetSportEventsRemovedLocale):
        offset (Union[Unset, int]):  Default: 0.
        start (Union[Unset, int]):  Default: 0.
        limit (Union[Unset, int]):  Default: 200.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSportEventsRemovedResponse200]
    """

    kwargs = _get_kwargs(locale=locale, offset=offset, start=start, limit=limit, format=format)

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    locale: GetSportEventsRemovedLocale,
    *,
    client: AuthenticatedClient,
    offset: Union[Unset, int] = 0,
    start: Union[Unset, int] = 0,
    limit: Union[Unset, int] = 200,
    format: str = "json",  # Added format parameter to async shorthand function
) -> Optional[GetSportEventsRemovedResponse200]:
    """sport events which has been removed

     Lists sport events which has been removed or disabled.

    Args:
        locale (GetSportEventsRemovedLocale):
        offset (Union[Unset, int]):  Default: 0.
        start (Union[Unset, int]):  Default: 0.
        limit (Union[Unset, int]):  Default: 200.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSportEventsRemovedResponse200
    """

    return (
        await asyncio_detailed(
            locale=locale,
            client=client,
            offset=offset,
            start=start,
            limit=limit,
            format=format,  # Pass format to asyncio_detailed
        )
    ).parsed
