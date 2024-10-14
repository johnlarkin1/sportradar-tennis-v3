from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_season_competitors_locale import GetSeasonCompetitorsLocale
from ...models.get_season_competitors_response_200 import GetSeasonCompetitorsResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    locale: GetSeasonCompetitorsLocale,
    urn_season: str,
    *,
    offset: Union[Unset, int] = 0,
    limit: Union[Unset, int] = 1000,
    start: Union[Unset, int] = 0,
    format: str = "json",  # Added format parameter with default "json"
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["offset"] = offset

    params["limit"] = limit

    params["start"] = start

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/{locale}/seasons/{urn_season}/competitors" + f".{format}",  # Append format to URL
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[GetSeasonCompetitorsResponse200]:
    if response.status_code == HTTPStatus.OK:
        response_200 = GetSeasonCompetitorsResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[GetSeasonCompetitorsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    locale: GetSeasonCompetitorsLocale,
    urn_season: str,
    *,
    client: AuthenticatedClient,
    offset: Union[Unset, int] = 0,
    limit: Union[Unset, int] = 1000,
    start: Union[Unset, int] = 0,
    format: str = "json",  # Added format parameter with default "json"
) -> Response[GetSeasonCompetitorsResponse200]:
    """get a list of competitors in a season

     Get a list of competitors in a season

    Args:
        locale (GetSeasonCompetitorsLocale):
        urn_season (str):
        offset (Union[Unset, int]):  Default: 0.
        limit (Union[Unset, int]):  Default: 1000.
        start (Union[Unset, int]):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSeasonCompetitorsResponse200]
    """

    kwargs = _get_kwargs(locale=locale, urn_season=urn_season, offset=offset, limit=limit, start=start, format=format)

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    locale: GetSeasonCompetitorsLocale,
    urn_season: str,
    *,
    client: AuthenticatedClient,
    offset: Union[Unset, int] = 0,
    limit: Union[Unset, int] = 1000,
    start: Union[Unset, int] = 0,
    format: str = "json",  # Added format parameter to shorthand function as well
) -> Optional[GetSeasonCompetitorsResponse200]:
    """get a list of competitors in a season

     Get a list of competitors in a season

    Args:
        locale (GetSeasonCompetitorsLocale):
        urn_season (str):
        offset (Union[Unset, int]):  Default: 0.
        limit (Union[Unset, int]):  Default: 1000.
        start (Union[Unset, int]):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSeasonCompetitorsResponse200
    """

    return sync_detailed(
        locale=locale,
        urn_season=urn_season,
        client=client,
        offset=offset,
        limit=limit,
        start=start,
        format=format,  # Pass format to sync_detailed
    ).parsed


async def asyncio_detailed(
    locale: GetSeasonCompetitorsLocale,
    urn_season: str,
    *,
    client: AuthenticatedClient,
    offset: Union[Unset, int] = 0,
    limit: Union[Unset, int] = 1000,
    start: Union[Unset, int] = 0,
    format: str = "json",  # Added format parameter with default "json"
) -> Response[GetSeasonCompetitorsResponse200]:
    """get a list of competitors in a season

     Get a list of competitors in a season

    Args:
        locale (GetSeasonCompetitorsLocale):
        urn_season (str):
        offset (Union[Unset, int]):  Default: 0.
        limit (Union[Unset, int]):  Default: 1000.
        start (Union[Unset, int]):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSeasonCompetitorsResponse200]
    """

    kwargs = _get_kwargs(locale=locale, urn_season=urn_season, offset=offset, limit=limit, start=start, format=format)

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    locale: GetSeasonCompetitorsLocale,
    urn_season: str,
    *,
    client: AuthenticatedClient,
    offset: Union[Unset, int] = 0,
    limit: Union[Unset, int] = 1000,
    start: Union[Unset, int] = 0,
    format: str = "json",  # Added format parameter to async shorthand function
) -> Optional[GetSeasonCompetitorsResponse200]:
    """get a list of competitors in a season

     Get a list of competitors in a season

    Args:
        locale (GetSeasonCompetitorsLocale):
        urn_season (str):
        offset (Union[Unset, int]):  Default: 0.
        limit (Union[Unset, int]):  Default: 1000.
        start (Union[Unset, int]):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSeasonCompetitorsResponse200
    """

    return (
        await asyncio_detailed(
            locale=locale,
            urn_season=urn_season,
            client=client,
            offset=offset,
            limit=limit,
            start=start,
            format=format,  # Pass format to asyncio_detailed
        )
    ).parsed
