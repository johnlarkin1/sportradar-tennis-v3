from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_sport_events_updated_locale import GetSportEventsUpdatedLocale
from ...models.get_sport_events_updated_response_200 import GetSportEventsUpdatedResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    locale: GetSportEventsUpdatedLocale,
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
        "url": f"/{locale}/sport_events/updated" + f".{format}",  # Append format to URL
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[GetSportEventsUpdatedResponse200]:
    if response.status_code == HTTPStatus.OK:
        response_200 = GetSportEventsUpdatedResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[GetSportEventsUpdatedResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    locale: GetSportEventsUpdatedLocale,
    *,
    client: AuthenticatedClient,
    offset: Union[Unset, int] = 0,
    start: Union[Unset, int] = 0,
    limit: Union[Unset, int] = 200,
    format: str = "json",  # Added format parameter with default "json"
) -> Response[GetSportEventsUpdatedResponse200]:
    """sport events which has been updated the last 24 hours

     Lists sport events which has been updated the last 24 hours

    Args:
        locale (GetSportEventsUpdatedLocale):
        offset (Union[Unset, int]):  Default: 0.
        start (Union[Unset, int]):  Default: 0.
        limit (Union[Unset, int]):  Default: 200.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSportEventsUpdatedResponse200]
    """

    kwargs = _get_kwargs(locale=locale, offset=offset, start=start, limit=limit, format=format)

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    locale: GetSportEventsUpdatedLocale,
    *,
    client: AuthenticatedClient,
    offset: Union[Unset, int] = 0,
    start: Union[Unset, int] = 0,
    limit: Union[Unset, int] = 200,
    format: str = "json",  # Added format parameter to shorthand function as well
) -> Optional[GetSportEventsUpdatedResponse200]:
    """sport events which has been updated the last 24 hours

     Lists sport events which has been updated the last 24 hours

    Args:
        locale (GetSportEventsUpdatedLocale):
        offset (Union[Unset, int]):  Default: 0.
        start (Union[Unset, int]):  Default: 0.
        limit (Union[Unset, int]):  Default: 200.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSportEventsUpdatedResponse200
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
    locale: GetSportEventsUpdatedLocale,
    *,
    client: AuthenticatedClient,
    offset: Union[Unset, int] = 0,
    start: Union[Unset, int] = 0,
    limit: Union[Unset, int] = 200,
    format: str = "json",  # Added format parameter with default "json"
) -> Response[GetSportEventsUpdatedResponse200]:
    """sport events which has been updated the last 24 hours

     Lists sport events which has been updated the last 24 hours

    Args:
        locale (GetSportEventsUpdatedLocale):
        offset (Union[Unset, int]):  Default: 0.
        start (Union[Unset, int]):  Default: 0.
        limit (Union[Unset, int]):  Default: 200.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSportEventsUpdatedResponse200]
    """

    kwargs = _get_kwargs(locale=locale, offset=offset, start=start, limit=limit, format=format)

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    locale: GetSportEventsUpdatedLocale,
    *,
    client: AuthenticatedClient,
    offset: Union[Unset, int] = 0,
    start: Union[Unset, int] = 0,
    limit: Union[Unset, int] = 200,
    format: str = "json",  # Added format parameter to async shorthand function
) -> Optional[GetSportEventsUpdatedResponse200]:
    """sport events which has been updated the last 24 hours

     Lists sport events which has been updated the last 24 hours

    Args:
        locale (GetSportEventsUpdatedLocale):
        offset (Union[Unset, int]):  Default: 0.
        start (Union[Unset, int]):  Default: 0.
        limit (Union[Unset, int]):  Default: 200.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSportEventsUpdatedResponse200
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
