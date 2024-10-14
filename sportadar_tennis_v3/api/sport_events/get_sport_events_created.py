from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_sport_events_created_locale import GetSportEventsCreatedLocale
from ...types import UNSET, Response, Unset


def _get_kwargs(
    locale: GetSportEventsCreatedLocale,
    *,
    offset: Union[Unset, int] = 0,
    start: Union[Unset, int] = 0,
    limit: Union[Unset, int] = 200,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["offset"] = offset

    params["start"] = start

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/{locale}/sport_events/created",
        "params": params,
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
    locale: GetSportEventsCreatedLocale,
    *,
    client: AuthenticatedClient,
    offset: Union[Unset, int] = 0,
    start: Union[Unset, int] = 0,
    limit: Union[Unset, int] = 200,
) -> Response[Any]:
    """sport events which has been created the last 24 hours

     Lists sport events which has been created the last 24 hours

    Args:
        locale (GetSportEventsCreatedLocale):
        offset (Union[Unset, int]):  Default: 0.
        start (Union[Unset, int]):  Default: 0.
        limit (Union[Unset, int]):  Default: 200.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        locale=locale,
        offset=offset,
        start=start,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    locale: GetSportEventsCreatedLocale,
    *,
    client: AuthenticatedClient,
    offset: Union[Unset, int] = 0,
    start: Union[Unset, int] = 0,
    limit: Union[Unset, int] = 200,
) -> Response[Any]:
    """sport events which has been created the last 24 hours

     Lists sport events which has been created the last 24 hours

    Args:
        locale (GetSportEventsCreatedLocale):
        offset (Union[Unset, int]):  Default: 0.
        start (Union[Unset, int]):  Default: 0.
        limit (Union[Unset, int]):  Default: 200.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        locale=locale,
        offset=offset,
        start=start,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
