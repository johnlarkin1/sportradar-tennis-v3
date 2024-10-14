from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_season_summaries_locale import GetSeasonSummariesLocale
from ...types import UNSET, Response, Unset


def _get_kwargs(
    locale: GetSeasonSummariesLocale,
    urn_season: str,
    *,
    offset: Union[Unset, int] = 0,
    limit: Union[Unset, int] = UNSET,
    start: Union[Unset, int] = 0,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["offset"] = offset

    params["limit"] = limit

    params["start"] = start

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/{locale}/seasons/{urn_season}/summaries",
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
    locale: GetSeasonSummariesLocale,
    urn_season: str,
    *,
    client: AuthenticatedClient,
    offset: Union[Unset, int] = 0,
    limit: Union[Unset, int] = UNSET,
    start: Union[Unset, int] = 0,
) -> Response[Any]:
    """get a list of summaries for all sport events in a season (any status)

     Get a list of summaries for all sport events in a season (any status).

    Args:
        locale (GetSeasonSummariesLocale):
        urn_season (str):
        offset (Union[Unset, int]):  Default: 0.
        limit (Union[Unset, int]):
        start (Union[Unset, int]):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        locale=locale,
        urn_season=urn_season,
        offset=offset,
        limit=limit,
        start=start,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    locale: GetSeasonSummariesLocale,
    urn_season: str,
    *,
    client: AuthenticatedClient,
    offset: Union[Unset, int] = 0,
    limit: Union[Unset, int] = UNSET,
    start: Union[Unset, int] = 0,
) -> Response[Any]:
    """get a list of summaries for all sport events in a season (any status)

     Get a list of summaries for all sport events in a season (any status).

    Args:
        locale (GetSeasonSummariesLocale):
        urn_season (str):
        offset (Union[Unset, int]):  Default: 0.
        limit (Union[Unset, int]):
        start (Union[Unset, int]):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        locale=locale,
        urn_season=urn_season,
        offset=offset,
        limit=limit,
        start=start,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
